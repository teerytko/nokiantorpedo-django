'''
Created on 28.6.2012

@author: teerytko
'''

from django.conf.urls.defaults import patterns, url, include
urlpatterns = patterns('',
    url(r'rest', include('statistics.rest.urls')),
    url(r'/$', 'statistics.views.statistics', name='statistics'),
    url(r'players$', 'statistics.views.players', name='players'),

)
