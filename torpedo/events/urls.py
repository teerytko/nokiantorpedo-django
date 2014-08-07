'''
Created on 25.8.2012

@author: teerytko
'''

from django.conf.urls import patterns, url, include
from events.feed import EventsFeed

urlpatterns = patterns('',
    # ...
    url(r'^$', 'events.views.events_timeline', name='events_timeline'),
    url(r'^list$', 'events.views.events_list', name='events_list'),
    url(r'^timeline$', 'events.views.events_timeline', name='events_timeline'),
    url(r'^calendar$', 'events.views.events_calendar', name='events_calendar'),
    url(r'^rest', include('events.rest.urls')),
    (r'^feed/(?P<type>[^\/]*)/$', EventsFeed()),
    (r'^feed/$', EventsFeed()),
    #
)