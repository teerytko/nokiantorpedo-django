'''
Created on 25.8.2012

@author: teerytko
'''
from django.contrib.syndication.views import Feed
from events.models import Event
from django.utils import feedgenerator

class EventsFeed(Feed):
    title = "Events"
    link = "/feed/"
    subtitle = "Calendar Events."

    feed_type = feedgenerator.Atom1Feed

    def items(self):
        return Event.objects.order_by('date_start')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
#
    def item_pubdate(self, item):
        """
        Takes an item, as returned by items(), and returns the item's
        pubdate.
        """
        return item.date_start

#    def feed_guid(self, item):
#        return item.title