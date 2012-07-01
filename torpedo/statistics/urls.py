'''
Created on 28.6.2012

@author: teerytko
'''

from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from statistics.models import MyModel

class MyResource(ModelResource):
    model = MyModel

urlpatterns = patterns('',
    url(r'mymodel$', ListOrCreateModelView.as_view(resource=MyResource)),
    url(r'mymodel(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=MyResource)),
)
