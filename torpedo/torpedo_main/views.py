'''
Created on 7.7.2012

@author: teerytko
'''

from django.template import Context, loader
from django.http import HttpResponse
from torpedo_main.menu import get_menu 

def home(request):
    t = loader.get_template('index.html')
    menu = get_menu()
    menu.active = 'home'
    c = Context({
        'menu': menu
    })
    return HttpResponse(t.render(c))