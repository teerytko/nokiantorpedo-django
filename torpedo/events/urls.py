'''
Created on 25.8.2012

@author: teerytko
'''

from django.conf.urls import patterns, url, include
from events.feed import EventsFeed

urlpatterns = patterns('',
    # ...
    (r'^feed/$', EventsFeed()),
    # ...
)