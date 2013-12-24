from django.template import RequestContext, loader
from django.http import HttpResponse
from torpedo_main.menu import get_menu, RootMenu, MenuItem
from statistics.models import League, Player
from django.utils.translation import ugettext as _
from django.http.response import HttpResponseRedirect

menu = get_menu()

def rooturl(lid):
    return '/statistics/%s/' % lid

def resturl(lid):
    return '/statistics/%s/rest/' % lid

def get_breadcrums(request, league):
    parts = request.path.strip('/').split('/')
    breadcrumb = RootMenu()
    breadcrumb.children['statistics'] = MenuItem(name=_('Statistics'), href='/statistics/%s' % league)
    lobj = League.objects.get(id=league)
    breadcrumb.children['league'] = MenuItem(name=lobj.name, href='/statistics/%s' % league)
    for lobj in League.objects.all():
        breadcrumb.children['league'].children[lobj.name] = MenuItem(name=lobj.name, href='/statistics/%s/' % lobj.id)
    if len(parts) == 2: 
        breadcrumb.children['next'] = MenuItem(name=_('next'), href='/statistics/%s' % league)
        breadcrumb.children['next'].children['teams'] = MenuItem(name='Teams', href='/statistics/%s/teams' % league)
        breadcrumb.children['next'].children['games'] = MenuItem(name='Games', href='/statistics/%s/games' % league)
    elif parts[-1] == 'teams':
        breadcrumb.children['teams'] = MenuItem(name=_('Teams'), href='/statistics/%s/teams' % league)
        breadcrumb.children['teams'].children['games'] = MenuItem(name='Games', href='/statistics/%s/games' % league)
    elif parts[-1] == 'games':
        breadcrumb.children['games'] = MenuItem(name=_('Games'), href='/statistics/%s/games' % league)
        breadcrumb.children['games'].children['teams'] = MenuItem(name='Teams', href='/statistics/%s/teams' % league)
    elif parts[-1] == 'team':
        breadcrumb.children['teams'] = MenuItem(name=_('Teams'), href='/statistics/%s/teams' % league)
        breadcrumb.children['teams'].children['games'] = MenuItem(name='Games', href='/statistics/%s/games' % league)
        breadcrumb.children['team'] = MenuItem(name=_('Team'), href='/statistics/%s/team' % league)
    elif parts[-1] == 'game':
        breadcrumb.children['games'] = MenuItem(name=_('Games'), href='/statistics/%s/games' % league)
        breadcrumb.children['games'].children['teams'] = MenuItem(name='Teams', href='/statistics/%s/teams' % league)
        breadcrumb.children['game'] = MenuItem(name=_('Game'), href='#')

    return breadcrumb

def default(request):
    last = League.objects.latest(field_name='id')
    return HttpResponseRedirect('%s%s' % (request.path, last.id))

def statistics(request, league):
    t = loader.get_template('statistics/main.html')
    menu.active = 'manage'
    l = League.objects.get(id=league)
    c = RequestContext(request, {
        'menu': menu,
        'league': l,
        'leagues': League.objects.all(),
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def players(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/players.html')
    menu.active = 'statistics'
    c = RequestContext(request, {
        'menu': menu,
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def games(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/games.html')
    menu.active = 'team'
    c = RequestContext(request, {
        'menu': menu,
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def teams(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/teams.html')
    menu.active = 'team'
    c = RequestContext(request, {
        'menu': menu,
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def team(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/team.html')
    menu.active = 'team'
    c = RequestContext(request, {
        'menu': menu,
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def game(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/game.html')
    menu.active = 'team'
    c = RequestContext(request, {
        'menu': menu,
        'league': l,
        'source': resturl(league),
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))

def players_dlg(request, league):
    l = League.objects.get(id=league)
    t = loader.get_template('statistics/players_dlg.html')
    menu.active = 'statistics'
    players = Player.objects.all()
    c = RequestContext(request, {
        'menu': menu,
        'league': l,
        'source': resturl(league),
        'players': players,
        'breadcrumbs': get_breadcrums(request, league)
    })
    return HttpResponse(t.render(c))
