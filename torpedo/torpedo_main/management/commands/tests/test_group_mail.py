# coding: utf8
'''
Created on Dec 8, 2013

@author: tsrytkon
'''

import os

from django.test import TestCase

from email import Message
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage

from torpedo_main.management.commands.group_mail import Command

CURDIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURDIR, 'multipartmail.txt')) as f:
    multipart_maildata = f.read()

class TestGroupMailCommand(TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_parse_email(self):
        cm = Command()
        ret = cm.parse_email(multipart_maildata)
        textcontent = cm.get_content_with_type(ret)
        self.assertEqual(ret['subject'], 'test 2')
        self.assertEqual(textcontent, """
Another Test!

-öt
""")

    def test_parse_email_html(self):
        cm = Command()
        ret = cm.parse_email(multipart_maildata)
        htmlcontent = cm.get_content_with_type(ret, 'text/html')
        self.assertEqual(htmlcontent, """\n<div dir="ltr">Another Test!<div><br></div><div>-öt</div></div>\n""")