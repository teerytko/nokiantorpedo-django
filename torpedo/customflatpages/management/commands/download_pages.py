#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import re
import optparse
import datetime
import socket
import traceback
import sys
import codecs
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.contrib.flatpages.models import FlatPage

VERSION = '0.1.0'

#~
class Command(BaseCommand):
    args = ''
    help = 'Sync flatpages'
    option_list = BaseCommand.option_list + (
        make_option('-p', '--pages',
                    help='The folder where the pages are downloaded.',
                    default='pages'),
        make_option('-r', '--regex',
                    help='The regex to page urls to download.',
                    default='.*'),
        )
    def ensure_dir_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def handle(self, *args, **options):
        """
        Synchronize the flatpages to a folder structure and back to database.
        """
        download_path = os.path.join(os.curdir, options['pages'])
        self.ensure_dir_exists(download_path)
        for flatpage in FlatPage.objects.all():
            if re.match(options['regex'], flatpage.url):
                print "Handling -", flatpage
                pagepath = os.path.join(download_path, 
                                        flatpage.url.rstrip('/').lstrip('/'))
                pagepath += '.html'
                pagedir = os.path.dirname(pagepath)
                self.ensure_dir_exists(pagedir)
                with codecs.open(pagepath, 'w', 'utf8') as pf:
                    pf.write(flatpage.content)
                    pf.close()
