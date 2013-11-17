'''
Created on Nov 17, 2013

@author: tsrytkon
'''
from django.conf.urls import patterns

urlpatterns = patterns('customflatpages.views',
    (r'^list$', 'list'),
    (r'^(?P<url>.*)$', 'flatpage'),
)
