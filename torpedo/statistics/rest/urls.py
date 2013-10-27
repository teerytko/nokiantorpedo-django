'''
Created on 28.6.2012

@author: teerytko
'''

from django.conf.urls import patterns, url
from djangorestframework.resources import ModelResource
from statistics.models import Team, League, Game, Player, Goal, Penalty
from statistics.rest.views import ListSearchModelView, MyInstanceModelView

class StatisticsBaseResource(ModelResource):
    """ Exclude only pk so that id is shown """
    exclude = ('pk')
    allow_unknown_form_fields = True


class TeamResource(StatisticsBaseResource):
    model = Team


class LeagueResource(StatisticsBaseResource):
    model = League


class GameResource(StatisticsBaseResource):
    model = Game
    include = list(StatisticsBaseResource.include) + ['home_goals', 'guest_goals']


class PlayerResource(StatisticsBaseResource):
    model = Player
    include = list(StatisticsBaseResource.include) + ['team_name', 'goals', 'assists',
                                             'penalties', 'points']

class GoalResource(StatisticsBaseResource):
    model = Goal


class PenaltyResource(StatisticsBaseResource):
    model = Penalty


urlpatterns = patterns('',
    url(r'league$', ListSearchModelView.as_view(resource=LeagueResource)),
    url(r'league/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=LeagueResource)),
    url(r'team$', ListSearchModelView.as_view(resource=TeamResource)),
    url(r'team/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=TeamResource)),
    url(r'game$', ListSearchModelView.as_view(resource=GameResource)),
    url(r'game/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=GameResource)),
    url(r'player$', ListSearchModelView.as_view(resource=PlayerResource)),
    url(r'player/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=PlayerResource)),
    url(r'goal$', ListSearchModelView.as_view(resource=GoalResource)),
    url(r'goal/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=GoalResource)),
    url(r'penalty$', ListSearchModelView.as_view(resource=PenaltyResource)),
    url(r'penalty/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=PenaltyResource)),
)
    