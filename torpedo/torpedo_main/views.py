'''
Created on 7.7.2012

@author: teerytko
'''

from django.template import RequestContext, loader
from django.http import HttpResponse
from torpedo_main.menu import get_menu 
from forms import UserProfileForm
from django.http import HttpResponseRedirect
from django_authopenid.views import signin as authsignin
from statistics.models import Team

def signin(request, *args, **kwargs):
    menu = get_menu()
    menu.active = None
    kwargs['extra_context'] = {
        'menu': menu
    }
    return authsignin(request, *args, **kwargs)

def home(request):
    t = loader.get_template('torpedo/index.html')
    menu = get_menu()
    menu.active = 'home'
    c = RequestContext(request, {
        'menu': menu
    })
    return HttpResponse(t.render(c))

def floorball_view(request, view):
    if view == '':
        view = 'main'
    t = loader.get_template('torpedo/floorball_%s.html' % view)
    menu = get_menu()
    menu.active = 'floorball'
    team= Team.objects.get(name='Nokian Torpedo')
    c = RequestContext(request, {
        'menu': menu,
        'team': team,
        'players': team.player.all().order_by('number'),
        
    })
    return HttpResponse(t.render(c))

def endurance_view(request, view):
    if view == '':
        view = 'main'
    t = loader.get_template('torpedo/endurance_%s.html' % view)
    menu = get_menu()
    menu.active = 'endurance'
    c = RequestContext(request, {
        'menu': menu,
    })
    return HttpResponse(t.render(c))


def calendar(request):
    t = loader.get_template('torpedo/calendar.html')
    menu = get_menu()
    menu.active = 'calendar'
    c = RequestContext(request, {
        'menu': menu
    })
    return HttpResponse(t.render(c))

def association(request):
    t = loader.get_template('torpedo/association.html')
    menu = get_menu()
    menu.active = 'association'
    c = RequestContext(request, {
        'menu': menu
    })
    return HttpResponse(t.render(c))

def profile(request):
    t = loader.get_template('torpedo/profile.html')
    user = request.user 
    user_profile = user.profile
    menu = get_menu()
    if request.method == 'POST': # If the form has been submitted...
        form = UserProfileForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user_profile.phonenumber = form.cleaned_data['phonenumber']
            user.save()
            user_profile.save()
            return HttpResponseRedirect('/') # Redirect after POST
        else:
            print form
    else:
        form = UserProfileForm(
            initial={'firstname': user.first_name,
                     'lastname': user.last_name,
                     'email': user.email,
                     'phonenumber': user.profile.phonenumber,
                     })
    c = RequestContext(request, {
        'form': form,
        'menu': menu
    })
    return HttpResponse(t.render(c))

