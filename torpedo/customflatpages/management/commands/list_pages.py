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
    help = 'List flatpages'
    option_list = BaseCommand.option_list + (
        )

    def handle(self, *args, **options):
        """
        """
        for flatpage in FlatPage.objects.all():
            print flatpage
