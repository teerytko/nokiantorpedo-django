#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
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
    help = 'Download flatpages'
    option_list = BaseCommand.option_list + (
        make_option('-p', '--pages',
                    help='The folder where the pages are uploaded.',
                    default='pages'),
        make_option('-r', '--regex',
                    help='The regex to pages to upload.',
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
        for root, dirs, files in os.walk(download_path):
            print "path:", root
            for fp in files:
                pagepath = os.path.join(root, fp)
                print "  file:", pagepath
                # Format the path to url
                if re.match(options['regex'], pagepath):
                    pageurl = os.path.join(root.replace(download_path, '').lstrip('/'), fp)
                    pageurl, _ = os.path.splitext(pageurl)
                    pageurl = '/' + pageurl + '/'
                    print "Uploading to url:", pageurl
                    with codecs.open(pagepath, 'r', 'utf8') as pf:
                        flatpage, created = FlatPage.objects.get_or_create(url=pageurl)
                        flatpage.content = pf.read()
                        flatpage.save()
                        pf.close()
