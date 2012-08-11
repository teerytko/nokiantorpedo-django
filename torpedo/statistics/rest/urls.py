'''
Created on 28.6.2012

@author: teerytko
'''

from django.conf.urls.defaults import patterns, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView
from statistics.models import Team, League, Game, Player, Goal, Penalty
from statistics.rest.views import ListSearchModelView, MyInstanceModelView


class TeamResource(ModelResource):
    model = Team


class LeagueResource(ModelResource):
    model = League


class GameResource(ModelResource):
    model = Game


class PlayerResource(ModelResource):
    model = Player
    exclude = ('pk')
    include = list(ModelResource.include) + ['team_name', 'goals', 'assists',
                                             'penalties', 'points']

class GoalResource(ModelResource):
    model = Goal


class PenaltyResource(ModelResource):
    model = Penalty


urlpatterns = patterns('',
    url(r'league$', ListSearchModelView.as_view(resource=LeagueResource)),
    url(r'league/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=LeagueResource)),
    url(r'team$', ListSearchModelView.as_view(resource=TeamResource)),
    url(r'team/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=TeamResource)),
    url(r'game', ListSearchModelView.as_view(resource=GameResource)),
    url(r'game/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=GameResource)),
    url(r'player$', ListSearchModelView.as_view(resource=PlayerResource)),
    url(r'player/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=PlayerResource)),
    url(r'goal$', ListSearchModelView.as_view(resource=GoalResource)),
    url(r'goal/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=GoalResource)),
    url(r'penalty$', ListSearchModelView.as_view(resource=PenaltyResource)),
    url(r'penalty/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=PenaltyResource)),
)
