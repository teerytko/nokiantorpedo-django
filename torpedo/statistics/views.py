from django.template import RequestContext, loader
from django.http import HttpResponse
from torpedo_main.menu import get_menu 

menu = get_menu()

def statistics(request):
    t = loader.get_template('statistics/main.html')
    menu.active = 'statistics'
    c = RequestContext(request, {
        'menu': menu
    })
    return HttpResponse(t.render(c))

def players(request):
    t = loader.get_template('statistics/players.html')
    menu.active = 'statistics'
    c = RequestContext(request, {
        'menu': menu
    })
    return HttpResponse(t.render(c))

def games(request):
    t = loader.get_template('statistics/games.html')
    menu.active = 'statistics'
    c = RequestContext(request, {
        'menu': menu
    })
    return HttpResponse(t.render(c))