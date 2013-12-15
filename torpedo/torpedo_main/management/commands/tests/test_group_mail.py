# coding: utf8
'''
Created on Dec 8, 2013

@author: tsrytkon
'''

from django.test import TestCase

from email import Message
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage

from torpedo_main.management.commands.group_mail import Command


multipart_maildata = """From teemu.rytkonen@gmail.com  Sun Dec  1 18:03:01 2013
Return-Path: <teemu.rytkonen@gmail.com>
X-Original-To: script-97930c853bb566540224a9dd8522b08687b24043@mx9.webfaction.com
Delivered-To: script-97930c853bb566540224a9dd8522b08687b24043@mx9.webfaction.com
Received: from localhost (localhost.localdomain [127.0.0.1])
    by mx9.webfaction.com (Postfix) with ESMTP id 5BB3A1A38A8CD;
    Sun,  1 Dec 2013 18:03:01 +0000 (UTC)
X-Spam-Flag: NO
X-Spam-Score: -1.398
X-Spam-Level: 
X-Spam-Status: No, score=-1.398 tagged_above=-999 required=3
    tests=[BAYES_00=-1.9, FREEMAIL_FROM=0.001, HTML_MESSAGE=0.001,
    RCVD_IN_DNSWL_NONE=-0.0001, T_DKIM_INVALID=0.5]
Received: from mx9.webfaction.com ([127.0.0.1])
    by localhost (mail9.webfaction.com [127.0.0.1]) (amavisd-new, port 10024)
    with ESMTP id BGlFMF8tzaru; Sun,  1 Dec 2013 18:03:00 +0000 (UTC)
Received: from mail-pd0-f182.google.com (mail-pd0-f182.google.com [209.85.192.182])
    by mx9.webfaction.com (Postfix) with ESMTP id CF0A01A38A890
    for <terd@nokiantorpedo.fi>; Sun,  1 Dec 2013 18:03:00 +0000 (UTC)
Received: by mail-pd0-f182.google.com with SMTP id v10so16524358pde.41
        for <terd@nokiantorpedo.fi>; Sun, 01 Dec 2013 10:03:00 -0800 (PST)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20120113;
        h=mime-version:date:message-id:subject:from:to:content-type;
        bh=La50/nqjGj8Hyw6tRgofxB89KsbUtDA0BXntk4FhZkw=;
        b=wbjaK6yTxlo9YIOcSk1wF6OKTjcssb/s0qGpXnSjfBRPmKymWyUNWb8/FRW8/xQwe5
         ifZqe5lSfZShw2OplgXmpK95XZGa3pLpc/D8/2ZLYiPrq3P7+I1/K0HN/GpeiEMQ/D5K
         0dHo19C3I3bhwMxkm83v07CwCecGwY9rKOXdczso22ItsLJnQuurZTi/Ds06TJbaQp19
         imFYmUScTZLN7qk7I7CtR22+eCE7vmaK4GAXUCQsN0tViYMNdZtIZSFPKtrahhRjlsTB
         4TOvakrYXwEaYpKVc/uifl5ig9lemyjmg1wnqWD6L7UOsjtK5habsKkg9FKdwSDiQzyT
         O3YA==
MIME-Version: 1.0
X-Received: by 10.68.129.201 with SMTP id ny9mr27230167pbb.70.1385920980096;
 Sun, 01 Dec 2013 10:03:00 -0800 (PST)
Received: by 10.68.128.196 with HTTP; Sun, 1 Dec 2013 10:02:59 -0800 (PST)
Date: Sun, 1 Dec 2013 20:02:59 +0200
Message-ID: <CAEZ8r2vSb5eTkTSn30kSCmn=9i1uOgWQa6sa-S4syShmok6r5w@mail.gmail.com>
Subject: test 2
From: =?ISO-8859-1?Q?Teemu_Rytk=F6nen?= <teemu.rytkonen@gmail.com>
To: terd@nokiantorpedo.fi
Content-Type: multipart/alternative; boundary=047d7b10cae5b49e9804ec7cdfa8

--047d7b10cae5b49e9804ec7cdfa8
Content-Type: text/plain; charset=ISO-8859-1

Another Test!

-öt

--047d7b10cae5b49e9804ec7cdfa8
Content-Type: text/html; charset=ISO-8859-1

<div dir="ltr">Another Test!<div><br></div><div>-öt</div></div>

--047d7b10cae5b49e9804ec7cdfa8--
"""

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