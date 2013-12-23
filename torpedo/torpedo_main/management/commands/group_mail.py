#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
events
Teemu Rytkönen
Group mail. Send mail to group of users fetched from db.
"""

import os
import re
import time
import optparse
import datetime
import socket
import traceback
import sys
from optparse import make_option
import email
from email.Iterators import typed_subpart_iterator
from email.header import decode_header

from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from torpedo_main.models import Section


class Command(BaseCommand):
    args = 'section'
    help = 'Send mail to Section.'
    option_list = BaseCommand.option_list + (
                        make_option('--list-sections',
                                    action='store_true',
                                    default=False,
                                    help='List available section.'),
                        make_option('--input',
                                    help='Input file.',
                                    default=None),
                        )

    def get_section(self, *args):
        try:
            return args[0]
        except IndexError:
            print "No section provided!"
            raise

    def list_sections(self):
        print "Sections:"
        for sectionname in Section.objects.all():
            print sectionname

    def send_mail(self, *args, **options):
        users = []
        sectionname = self.get_section(*args)
        # find users for the given section
        section = Section.objects.get(group__name__iexact=sectionname)
        print "Section: ", section 
        for user in User.objects.all():
            if user.memberprofile.memberof.filter(id=section.id).exists():
                users.append(user)
        if options['input']:
            with open(options['input']) as inf:
                data = inf.read()
        else:
            data = sys.stdin.read()
        print data
        edata = self.parse_email(data)
        maincontent = self.get_content_with_type(edata)
        sectionemail = "%s@nokiantorpedo.fi" % section
        fromemail = self.getheader(edata.get('From'))
        fromemail = re.match('.*<(.*)>', fromemail).group(1)
        tousers = [user.email for user in users] # if user.email != fromemail]
        subject = self.getheader(edata['subject'])
        headers = {'Reply-To': sectionemail}
        em = EmailMultiAlternatives(subject=subject,
                          body=maincontent,
                          to=tousers,
                          from_email=fromemail,
                          headers=headers)
        if edata.is_multipart() and self.get_content_with_type(edata):
            htmlcontent = self.get_content_with_type(edata, 'text/html')
            em.attach_alternative(htmlcontent, 'text/html')
        em.send(True)

    def parse_email(self, data):
        """
        parse email subject, content from data.
        """
        return email.message_from_string(data)

    def getheader(self, header_text, default="ascii"):
        """Decode the specified header"""
        headers = decode_header(header_text)
        header_sections = [unicode(text.replace('\n', ''), charset or default)
                           for text, charset in headers]
        return u"".join(header_sections)

    def get_charset(self, message, default="ascii"):
        """Get the message charset"""
        if message.get_content_charset():
            return message.get_content_charset()
        if message.get_charset():
            return message.get_charset()
        return default

    def get_content_with_type(self, message, contenttype='text/plain'):
        """
        parse email subject, content from data.
        """
        maintype, subtype = contenttype.split('/')
        parts = [part
                      for part in typed_subpart_iterator(message,
                                                         maintype,
                                                         subtype)]
        body = []
        for part in parts:
            charset = self.get_charset(part, self.get_charset(message))
            body.append(unicode(part.get_payload(decode=True),
                                charset,
                                "replace"))
        return u"\n".join(body).strip()

    def get_headers(self, ep):
        """
        parse email subject, content from data.
        """
        return dict([(item[0], self.getheader(item[1])) for item in ep.items()])

    def handle(self, *args, **options):
        if (options['list_sections']):
            self.list_sections()
        else:
            self.send_mail(*args, **options)
