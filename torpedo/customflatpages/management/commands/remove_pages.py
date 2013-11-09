#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import optparse
import datetime
import socket
import traceback
import sys
import codecs
import re
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.contrib.flatpages.models import FlatPage

VERSION = '0.1.0'

#~
class Command(BaseCommand):
    args = ''
    help = 'Remove flatpages'
    option_list = BaseCommand.option_list + (
        make_option('-r', '--regex',
                    help='The regex to page urls to remove.',
                    default='.*'),
        make_option('-n', '--dry-run',
                    action='store_true',
                    help='Only print actions, does not actually remove anything.',
                    default=False),
        )

    def handle(self, *args, **options):
        """
        """
        for flatpage in FlatPage.objects.all():
            print "Checking -", flatpage
            if re.match(options['regex'], flatpage.url):
                print "Removing -", flatpage
                if not options['dry_run']:
                    flatpage.delete()
