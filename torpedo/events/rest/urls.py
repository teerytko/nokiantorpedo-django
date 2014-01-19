'''
Created on 28.6.2012

@author: teerytko
'''

from django.conf.urls import patterns, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView
from events.models import Event, OsallistujatEvent, SportsEvent
from statistics.rest.views import ListSearchModelView, MyInstanceModelView

class BaseResource(ModelResource):
    """ Exclude only pk so that id is shown """
    exclude = ('pk')
    allow_unknown_form_fields = True


class EventResource(BaseResource):
    include = ('duration', 'url', )
    model = Event

class SportsEventResource(BaseResource):
    model = SportsEvent

class OsallistujatEventResource(BaseResource):
    model = OsallistujatEvent


urlpatterns = patterns('',
    url(r'event$', ListSearchModelView.as_view(resource=EventResource)),
    url(r'event/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=EventResource)),
    url(r'sportsevent$', ListSearchModelView.as_view(resource=SportsEventResource)),
    url(r'sportsevent/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=SportsEventResource)),
    url(r'oevent$', ListSearchModelView.as_view(resource=OsallistujatEventResource)),
    url(r'oevent/(?P<pk>[^/]+)/$', MyInstanceModelView.as_view(resource=OsallistujatEventResource)),
)
