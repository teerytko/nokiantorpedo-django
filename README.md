nokiantorpedo-django
====================

Nokiantorpedo with django


Installation
------------
Prerequisites:
- python 2.6+ 
- pip

install requirements
--------------------

 pip install -r requirements_prod.txt


Development instance
--------------------

Run development server (uses sqlite db):

 python manage.py syncdb --settings=torpedo.dev_settings
 python manage.py migrate --settings=torpedo.dev_settings
 python manage.py runserver --settings=torpedo.dev_settings


Production instance
-------------------

Create mysql database:

 mysql
 create database torpedo_nt

 python manage.py syncdb --settings=torpedo.prod_settings
 python manage.py migrate --settings=torpedo.prod_settings
 python manage.py runserver --settings=torpedo.prod_settings


