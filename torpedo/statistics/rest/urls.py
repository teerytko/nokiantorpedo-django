'''
Created on 28.6.2012

@author: teerytko
'''

from django.conf.urls.defaults import patterns, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from statistics.models import Team, League, Game, Player, Goal, Penalty


class TeamResource(ModelResource):
    model = Team


class LeagueResource(ModelResource):
    model = League


class GameResource(ModelResource):
    model = Game


class PlayerResource(ModelResource):
    model = Player


class GoalResource(ModelResource):
    model = Goal


class PenaltyResource(ModelResource):
    model = Penalty

urlpatterns = patterns('',
    url(r'rest/league$', ListOrCreateModelView.as_view(resource=LeagueResource)),
    url(r'rest/league/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=LeagueResource)),
    url(r'rest/team$', ListOrCreateModelView.as_view(resource=TeamResource)),
    url(r'rest/team/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=TeamResource)),
    url(r'rest/game$', ListOrCreateModelView.as_view(resource=GameResource)),
    url(r'rest/game/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=GameResource)),
    url(r'rest/player$', ListOrCreateModelView.as_view(resource=PlayerResource)),
    url(r'rest/player/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=PlayerResource)),
    url(r'rest/goal$', ListOrCreateModelView.as_view(resource=GoalResource)),
    url(r'rest/goal/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=GoalResource)),
    url(r'rest/penalty$', ListOrCreateModelView.as_view(resource=PenaltyResource)),
    url(r'rest/penalty/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=PenaltyResource)),
)
