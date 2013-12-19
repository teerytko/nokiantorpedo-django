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
        fromemail = edata.get('From')
        tousers = [user.email for user in users]
        print "Sending mail: %s" % edata['subject']
        print "Content:\n%s" % maincontent

        em = EmailMultiAlternatives(subject=edata['subject'],
                          body=maincontent,
                          to=tousers,
                          from_email=fromemail,
                          headers=dict(edata.items()))
        if edata.is_multipart() and self.get_content_with_type(edata):
            htmlcontent = self.get_content_with_type(edata, 'text/html')
            print "htmlcontent:\n%s" % htmlcontent

            em.attach_alternative(htmlcontent, 'text/html')
        em.send(True)

    def parse_email(self, data):
        """
        parse email subject, content from data.
        """
        return email.message_from_string(data)

    def get_content_with_type(self, ep, contenttype='text/plain'):
        """
        parse email subject, content from data.
        """
        for payload in ep.get_payload():
            _, typepart, content = unicode(payload).split('\n', 2)
            if typepart.find(contenttype) != -1:
                return content

    def handle(self, *args, **options):
        if (options['list_sections']):
            self.list_sections()
        else:
            self.send_mail(*args, **options)
