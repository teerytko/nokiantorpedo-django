# Create your views here.

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

from events.models import Event
from datetime import datetime


def events_calendar(request):
    events = Event.objects.all()
    t = loader.get_template('events/calendar.html')
    c = RequestContext(request, {
        'events': events
    })
    return HttpResponse(t.render(c))


def events_list(request):
    today = datetime.now()
    t = loader.get_template('events/list.html')
    c = RequestContext(request, {
    })
    return HttpResponse(t.render(c))
