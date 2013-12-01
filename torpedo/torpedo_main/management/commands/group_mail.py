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


from django.core.mail import send_mail, EmailMessage
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
        data = sys.stdin.read()
        edata, maincontent = self.parse_email(data)
        sender = "%s@nokiantorpedo.fi" % section
        tousers = [user.email for user in users]
        print "Sending mail: %s" % edata['subject']
        em = EmailMessage(subject=edata['subject'],
                          body=maincontent,
                          from_email=sender,
                          to=tousers)
        
        em.send(True)

    def parse_email(self, data):
        """
        parse email subject, content from data.
        """
        ep = email.message_from_string(data)
        content = str(ep.get_payload(0))
        return ep, content

    def handle(self, *args, **options):
        if (options['list_sections']):
            self.list_sections()
        else:
            self.send_mail(*args, **options)
