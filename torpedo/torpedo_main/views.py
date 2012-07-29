'''
Created on 7.7.2012

@author: teerytko
'''

from django.template import RequestContext, loader
from django.http import HttpResponse
from torpedo_main.menu import get_menu 

def home(request):
    t = loader.get_template('index.html')
    menu = get_menu()
    menu.active = 'home'
    c = RequestContext(request, {
        'menu': menu
    })
    return HttpResponse(t.render(c))

def association(request):
    t = loader.get_template('association.html')
    menu = get_menu()
    menu.active = 'association'
    c = RequestContext(request, {
        'menu': menu
    })
    return HttpResponse(t.render(c))

