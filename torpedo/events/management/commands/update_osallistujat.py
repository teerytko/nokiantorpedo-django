#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
events
Teemu Rytkönen
events update osallistujat
"""

import os
import time
import optparse
import datetime
import socket
import traceback
import sys
#TEMP
os.environ['HTTP_PROXY'] = ''

import feedparser
from django.core.management.base import BaseCommand, CommandError

try:
    import threadpool
except ImportError:
    threadpool = None

VERSION = '0.9.16'
URL = 'http://www.events.org/'
USER_AGENT = 'Feedjack %s - %s' % (VERSION, URL)
SLOWFEED_WARNING = 10
ENTRY_NEW, ENTRY_UPDATED, ENTRY_SAME, ENTRY_ERR = range(4)
FEED_OK, FEED_SAME, FEED_ERRPARSE, FEED_ERRHTTP, FEED_ERREXC = range(5)

def encode(tstr):
    """ Encodes a unicode string in utf-8
    """
    if not tstr:
        return ''
    # this is _not_ pretty, but it works
    try:
        return tstr.encode('utf-8', "xmlcharrefreplace")
    except UnicodeDecodeError:
        # it's already UTF8.. sigh
        return tstr.decode('utf-8').encode('utf-8')

def prints(tstr):
    """ lovely unicode
    """
    sys.stdout.write('%s\n' % (tstr.encode(sys.getdefaultencoding(),
                         'replace')))
    sys.stdout.flush()

def mtime(ttime):
    """ datetime auxiliar function.
    """
    return datetime.datetime.fromtimestamp(time.mktime(ttime))

class ProcessEntry:
    def __init__(self, feed, options, entry, postdict, fpf, fromtime):
        self.feed = feed
        self.options = options
        self.entry = entry
        self.postdict = postdict
        self.fpf = fpf
        self.fromtime = fromtime

    def get_entry_data(self):
        """ Retrieves data from a post and returns it in a tuple.
        """
        try:
            link = self.entry.link
        except AttributeError:
            link = self.feed.feed_url
        try:
            title = self.entry.title
        except AttributeError:
            title = link
        guid = title

        if self.entry.has_key('author_detail'):
            author = self.entry.author_detail.get('name', '')
            author_email = self.entry.author_detail.get('email', '')
        else:
            author, author_email = '', ''

        if not author:
            author = self.entry.get('author', self.entry.get('creator', ''))
        if not author_email:
            # this should be optional~
            author_email = 'nospam@nospam.com'
        
        try:
            content = self.entry.content[0].value
        except:
            content = self.entry.get('summary',
                                     self.entry.get('description', ''))
        
        try:
            # parse the specific osallistujat time
            dstr = title.split('-')[0].split(' ',1)[1]
            df = datetime.datetime.strptime(dstr, '%d.%m.%y %H:%M')
            date_start = df
        except:
            date_start = None

        comments = self.entry.get('comments', '')

        return (link, title, guid, author, author_email, content, 
                date_start, comments)

    def process(self):
        """ Process a post in a feed and saves it in the DB if necessary.
        """
        from events import models

        (link, title, guid, author, author_email, content, date_start,
         comments) = self.get_entry_data()
        # Ignore feed items where team is not Nokian Torpedo
        if not content.startswith('Joukkue: Nokian Torpedo'):
            return 0
        # skip entries that are older that fromtime
        if date_start < self.fromtime:
            return 0
        if guid in self.postdict:
            tobj = self.postdict[guid]
            if tobj.content != content or (date_start and
                    tobj.date_start != date_start):
                retval = ENTRY_UPDATED
                if self.options.verbose:
                    prints('[%d] Updating existing event: %s' % (
                           self.feed.id, link))
                if not date_start:
                    # damn non-standard feeds
                    date_start = tobj.date_start
                tobj.title = title
                tobj.link = link
                tobj.content = content
                tobj.guid = guid
                tobj.date_start = date_start
                tobj.author = author
                tobj.author_email = author_email
                tobj.comments = comments
                tobj.save()
            else:
                retval = ENTRY_SAME
                if self.options.verbose:
                    prints('[%d] Post has not changed: %s' % (self.feed.name,
                                                              link))
        else:
            retval = ENTRY_NEW
            if self.options.verbose:
                prints('[%d] Saving new post: %s' % (self.feed.name, link))
            if not date_start and self.fpf:
                # if the feed has no date_start info, we use the feed
                # mtime or the current time
                if self.fpf.feed.has_key('modified_parsed'):
                    date_start = mtime(self.fpf.feed.modified_parsed)
                elif self.fpf.has_key('modified'):
                    date_start = mtime(self.fpf.modified)
            if not date_start:
                date_start = datetime.datetime.now()
            tobj = models.Event(title=title, link=link,
                content=content, guid=guid, date_start=date_start,
                author=author, author_email=author_email,
                comments=comments)
            tobj.save()
        return retval


class ProcessFeed:
    def __init__(self, feed, options, fromtime):
        self.feed = feed
        self.options = options
        self.fromtime = fromtime
        self.fpf = None

    def process_entry(self, entry, postdict):
        """ wrapper for ProcessEntry
        """
        entry = ProcessEntry(self.feed, self.options, entry, postdict,
                             self.fpf, self.fromtime)
        ret_entry = entry.process()
        del entry
        return ret_entry

    def process(self):
        """ Downloads and parses a feed.
        """
        from events import models

        ret_values = {
            ENTRY_NEW:0,
            ENTRY_UPDATED:0,
            ENTRY_SAME:0,
            ENTRY_ERR:0}

        prints(u'[%s] Processing feed %s' % (self.feed.name,
                                             self.feed.feed_url))

        # we check the etag and the modified time to save bandwith and
        # avoid bans
        try:
            self.fpf = feedparser.parse(self.feed.feed_url,
                                        agent=USER_AGENT)
        except:
            prints('! ERROR: feed cannot be parsed')
            return FEED_ERRPARSE, ret_values
        
        if hasattr(self.fpf, 'status'):
            if self.options.verbose:
                prints(u'[%d] HTTP status %d: %s' % (self.feed.name,
                                                     self.fpf.status,
                                                     self.feed.feed_url))
            if self.fpf.status == 304:
                # this means the feed has not changed
                if self.options.verbose:
                    prints('[%d] Feed has not changed since ' \
                           'last check: %s' % (self.feed.name,
                                               self.feed.feed_url))
                return FEED_SAME, ret_values

            if self.fpf.status >= 400:
                # http error, ignore
                prints('[%d] !HTTP_ERROR! %d: %s' % (self.feed.name,
                                                     self.fpf.status,
                                                     self.feed.feed_url))
                return FEED_ERRHTTP, ret_values

        if hasattr(self.fpf, 'bozo') and self.fpf.bozo:
            prints('[%d] !BOZO! Feed is not well formed: %s' % (
                self.feed.name, self.feed.feed_url))
        
        if False and self.options.verbose:
            prints(u'[%d] Feed info for: %s\n' % (
                self.feed.name, self.feed.feed_url))
        #delete events that occur in past
        oldevents = models.Event.objects.filter(date_start__lte=self.fromtime)
        oldevents.delete()

        guids = []
        for entry in self.fpf.entries:
            if entry.title:
                guids.append(entry.title)
            elif entry.link:
                guids.append(entry.link)
        if guids:
            postdict = dict([(post.guid, post) 
              for post in models.Event.objects.filter(guid__in=guids)])
        else:
            postdict = {}

        for entry in self.fpf.entries:
            try:
                ret_entry = self.process_entry(entry, postdict)
            except:
                (etype, eobj, etb) = sys.exc_info()
                print '[%s] ! -------------------------' % (self.feed.name,)
                print traceback.format_exception(etype, eobj, etb)
                traceback.print_exception(etype, eobj, etb)
                print '[%s] ! -------------------------' % (self.feed.name,)
                ret_entry = ENTRY_ERR
            ret_values[ret_entry] += 1


        return FEED_OK, ret_values


class Feed():
    def __init__(self, name, url):
        self.name = name
        self.feed_url = url


def main():
    """ Main function. Nothing to see here. Move along.
    """
    parser = optparse.OptionParser(usage='%prog [options]',
                                   version=USER_AGENT)
    parser.add_option('--settings',
      help='Python path to settings module. If this isn\'t provided, ' \
           'the DJANGO_SETTINGS_MODULE enviroment variable will be used.')
    parser.add_option('-f', '--feed', action='append', type='int',
      help='A feed id to be updated. This option can be given multiple ' \
           'times to update several feeds at the same time ' \
           '(-f 1 -f 4 -f 7).')
    parser.add_option('-s', '--site', type='int',
      help='A site id to update.')
    parser.add_option('-v', '--verbose', action='store_true',
      dest='verbose', default=False, help='Verbose output.')
    parser.add_option('-t', '--timeout', type='int', default=10,
      help='Wait timeout in seconds when connecting to feeds.')
    parser.add_option('-w', '--workerthreads', type='int', default=10,
      help='Worker threads that will fetch feeds in parallel.')
    options = parser.parse_args()[0]
    if options.settings:
        os.environ["DJANGO_SETTINGS_MODULE"] = options.settings


    from events import models

    # settting socket timeout (default= 10 seconds)
    socket.setdefaulttimeout(options.timeout)
   
    now = datetime.datetime.now()
    prints('* BEGIN: %s' % (unicode(now),))

    feed = Feed('Osallistujat.com', 
         'http://www.osallistujat.com/RSS.php?id=1925&cal=h0g143ub5p')
    pfeed = ProcessFeed(feed, options, now)
    ret_feed, ret_entries = pfeed.process()
    del pfeed

if __name__ == '__main__':
    main()

#~
class Command(BaseCommand):
    args = ''
    help = 'Updates events'

    def handle(self, *args, **options):
        main()
