
import posixpath
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import get_current_site
from django.core.xheaders import populate_xheaders
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.template import loader, RequestContext
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect
from django.contrib.flatpages.forms import FlatpageForm
from django.http import HttpResponseRedirect
from django.template import Template, TemplateSyntaxError

from customflatpages.forms import ShortFlatpageForm
from torpedo_main.menu import get_menu
menu = get_menu()


def list(request):
    """
    """
    prefix = posixpath.abspath(posixpath.join(request.path, '..'))
    t = loader.get_template('flatpages/list.html')
    c = RequestContext(request,
                       {'urlprefix': prefix,
                        'menu': menu
                       })
    return HttpResponse(t.render(c))



# This view is called from FlatpageFallbackMiddleware.process_response
# when a 404 is raised, which often means CsrfViewMiddleware.process_view
# has not been called even if CsrfViewMiddleware is installed. So we need
# to use @csrf_protect, in case the template needs {% csrf_token %}.
# However, we can't just wrap this view; if no matching flatpage exists,
# or a redirect is required for authentication, the 404 needs to be returned
# without any CSRF checks. Therefore, we only
# CSRF protect the internal implementation.
def flatpage(request, url, **extra_content):
    """
    Public interface to the flat page view.

    Models: `flatpages.flatpages`
    Templates: Uses the template defined by the ``template_name`` field,
        or :template:`flatpages/default.html` if template_name is not defined.
    Context:
        flatpage
            `flatpages.flatpages` object
    """
    extra_content.setdefault('menu', menu)
    if request.GET.get('edit') == 'true':
        return flatpage_edit(request, url, **extra_content)
    elif request.GET.get('delete') == 'true':
        return flatpage_delete(request, url, **extra_content)
    else:
        return flatpage_show(request, url, **extra_content)


def flatpage_show(request, url, **extra_content):
    """
    """
    if not url.startswith('/'):
        url = '/' + url
    site_id = get_current_site(request).id
    try:
        f = get_object_or_404(FlatPage,
            url__exact=url, sites__id__exact=site_id)
    except Http404:
        return render_404_flatpage(request, **extra_content)
    return render_flatpage(request, f, **extra_content)

def flatpage_delete(request, url, **extra_content):
    """
    """
    prefix = request.path.replace(url, '')
    listurl = posixpath.join(prefix, 'list')
    if not url.startswith('/'):
        url = '/' + url
    site_id = get_current_site(request).id
    try:
        f = get_object_or_404(FlatPage,
            url__exact=url, sites__id__exact=site_id)
        f.delete()
    except Http404:
        return render_404_flatpage(request, **extra_content)
    return HttpResponseRedirect(listurl) # Redirect after POST


def base_content():
    try:
        return FlatPage.objects.get(url='/uusi').content
    except FlatPage.DoesNotExist:
        return ''


def flatpage_edit(request, url, **extra_content):
    t = loader.get_template('flatpages/edit.html')
    url = '/'+url
    site_id = get_current_site(request).id
    flatpage, created = FlatPage.objects.get_or_create(url=url)
    if created:
        flatpage.sites.add(site_id)
        flatpage.content = base_content()
        flatpage.title = url.replace('/', '')
    if request.method == 'POST': # If the form has been submitted...
        form = ShortFlatpageForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            flatpage.url = form.cleaned_data['url']
            flatpage.title = form.cleaned_data['title']
            flatpage.content = form.cleaned_data['content']
            flatpage.save()
            return HttpResponseRedirect(request.path) # Redirect after POST
    else:
        form = ShortFlatpageForm(
            initial={'url': flatpage.url,
                     'title': flatpage.title,
                     'content': flatpage.content,
                     })
    context = extra_content.copy()
    context['form'] = form
    context['title']= flatpage.title
    c = RequestContext(request, context)
    return HttpResponse(t.render(c))

@csrf_protect
def render_404_flatpage(request, **extra_content):
    """
    Internal interface to the flat page view.
    """
    t = loader.get_template('flatpages/404.html')
    context = extra_content.copy()
    c = RequestContext(request, context)
    return HttpResponse(t.render(c))

@csrf_protect
def render_flatpage(request, f, **extra_content):
    """
    Internal interface to the flat page view.
    """
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if f.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    f.title = mark_safe(f.title)
    t = Template(f.content)
    context = extra_content.copy()
    context['flatpage'] = f
    c = RequestContext(request, context)
    resp = t.render(c)
    response = HttpResponse(resp)
    populate_xheaders(request, response, FlatPage, f.id)
    return response


