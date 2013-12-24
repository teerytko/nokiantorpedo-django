#!/usr/bin/python
'''
Created on 7.7.2012

@author: teerytko
'''

import os

from django.conf import settings
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django_authopenid.views import signin as authsignin
from django.contrib.auth.models import User
from forms import UserProfileForm, UserImageForm, MemberProfileForm, \
TorpedoRegistrationForm, TorpedoAuthenticationForm
from registration.backends.default.views import RegistrationView
from customflatpages.views import flatpage


from torpedo_main.menu import get_menu
from statistics.models import Team, Player, Game

def media_file(name):
    return os.path.join(settings.MEDIA_ROOT, name)


def handle_uploaded_file(f):
    filepath = media_file(f.name)
    with open(filepath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f.name


def signin(request, *args, **kwargs):
    return authsignin(request, auth_form=TorpedoAuthenticationForm,
                      *args, **kwargs)


class TorpedoRegistrationView(RegistrationView):
    form_class = TorpedoRegistrationForm

    def get_context_data(self, **kwargs):
        menu = get_menu()
        menu.active = None
        kwargs['menu'] = menu
        return kwargs

def home(request):
    return flatpage(request, '/home/')


def floorball(request):
    team = Team.objects.get(name='Nokian Torpedo')
    players = Player.objects.filter(team=team).order_by('number')
    games = Game.objects.filter(league=team.league)
    return flatpage(request, '/floorball/', 
                    team=team,
                    players=players,
                    games=games)


def endurance(request):
    return flatpage(request, '/endurance/')


def manage(request):
    if request.user.is_staff:
        users = User.objects.all()
        return flatpage(request, '/manage/', 
                        users=users)
    else:
        raise PermissionDenied


def calendar(request):
    return flatpage(request, '/calendar/')


def association(request):
    menu = get_menu()
    menu.active = 'association'
    return flatpage(request, '/association/', 
                    menu=menu)

def channel(request):
    menu = get_menu()
    menu.active = 'home'
    return flatpage(request, '/channel/', 
                    menu=menu)

def profile(request, username=None):
    user = get_user(request, username)
    user_profile = user.profile
    return flatpage(request, '/profile/', 
                    profileuser=user)

def get_user(request, username=None):
    if username is None:
        user = request.user
    elif username == request.user.username:
        user = request.user
    else:
        if request.user.is_staff:
            user = User.objects.get(username=username)
        else:
            raise PermissionDenied
    return user

def profile_edit(request, username=None, dialog=False):
    if dialog is True:
        t = loader.get_template('torpedo/profile_dlg.html')
    else:
        t = loader.get_template('torpedo/profile.html')
    user = get_user(request, username)
    user_profile = user.profile
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
            return HttpResponseRedirect(request.META['HTTP_REFERER']) # Redirect after POST
    else:
        form = UserProfileForm(
            initial={'firstname': user.first_name,
                     'lastname': user.last_name,
                     'email': user.email,
                     'phonenumber': user.profile.phonenumber,
                     })
    c = RequestContext(request, {
        'form': form,
        'profileuser': user
    })
    return HttpResponse(t.render(c))


def member_edit(request, username=None, dialog=False):
    if dialog is True:
        t = loader.get_template('torpedo/profile_dlg.html')
    else:
        t = loader.get_template('torpedo/profile.html')
    user = get_user(request, username)
    member_profile = user.memberprofile
    if request.method == 'POST': # If the form has been submitted...
        form = MemberProfileForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            member_profile.payments = form.cleaned_data['payments']
            member_profile.memberof.clear()
            for membership in form.cleaned_data['memberof']:
                member_profile.memberof.add(membership)
            member_profile.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER']) # Redirect after POST
    else:
        form = MemberProfileForm(
            initial={'payments': member_profile.payments,
                     'memberof': member_profile.memberof.all(),
                     })
    if not request.user.is_staff:
        form.fields['payments'].widget.attrs['readonly'] = True
    c = RequestContext(request, {
        'form': form,
        'profileuser': user
    })
    return HttpResponse(t.render(c))

def profile_img(request, username=None, dialog=False):
    if dialog is True:
        t = loader.get_template('torpedo/profile_dlg.html')
    else:
        t = loader.get_template('torpedo/profile.html')
    user = get_user(request, username)
    user_profile = user.profile
    if request.method == 'POST': # If the form has been submitted...
        form = UserImageForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            filename = handle_uploaded_file(request.FILES['userimage'])
            user_profile.userimage = filename
            
            user.save()
            user_profile.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER']) # Redirect after POST
    else:
        form = UserImageForm(
            initial={'userimage': user.profile.userimage,
                     })
    c = RequestContext(request, {
        'form': form,
        'profileuser': user
    })
    return HttpResponse(t.render(c))


