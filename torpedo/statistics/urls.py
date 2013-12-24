'''
Created on 28.6.2012

@author: teerytko
'''

from django.conf.urls import patterns, url, include
urlpatterns = patterns('',
    url(r'(?P<league>\d+)/rest', include('statistics.rest.urls')),
    url(r'(?P<league>\d+)/$', 'statistics.views.statistics', name='statistics'),
    url(r'(?P<league>\d+)/players$', 'statistics.views.players', name='players'),
    url(r'(?P<league>\d+)/game$', 'statistics.views.game', name='game'),
    url(r'(?P<league>\d+)/games$', 'statistics.views.games', name='games'),
    url(r'(?P<league>\d+)/team$', 'statistics.views.team', name='team'),
    url(r'(?P<league>\d+)/teams$', 'statistics.views.teams', name='teams'),
    url(r'/$', 'statistics.views.default'),
)
