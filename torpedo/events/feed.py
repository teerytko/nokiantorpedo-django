'''
Created on 25.8.2012

@author: teerytko
'''
from django.contrib.syndication.views import Feed
from events.models import Event
from django.utils import feedgenerator

class EventsFeed(Feed):
    title = "Tapahtumat"
    link = "/feed/"
    subtitle = "Calendar Events."

    feed_type = feedgenerator.Atom1Feed

    def get_object(self,  request, *args, **kwargs):
        if kwargs.has_key('type'):
            return Event.objects.filter(type=kwargs['type'])
        else:
            return None

    def items(self, obj):
        if obj is not None:
            return obj.order_by('start_date')[:5]
        else:
            return Event.objects.order_by('start_date')[:5]

    def item_title(self, item):
        return "%s %s" % (item.start_date, item.title)

    def item_description(self, item):
        return item.description
#
    def item_pubdate(self, item):
        """
        Takes an item, as returned by items(), and returns the item's
        pubdate.
        """
        return item.start_date

    def item_link(self, item):
        return item.link or ''

#    def feed_guid(self, item):
#        return item.title