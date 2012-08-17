# Development settings file
#

import os
CURDIR = os.path.dirname(__file__)
execfile(os.path.join(CURDIR, 'settings.py'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'teerytko_nt',                      # Or path to database file if using sqlite3.
        'USER': 'teerytko_nt',                      # Not used with sqlite3.
        'PASSWORD': 'torpedo',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


MEDIA_ROOT = '/home/teerytko/webapps/torpedo_static/media'
MEDIA_URL = '/torpedo/media/'
STATIC_ROOT = '/home/teerytko/webapps/torpedo_static/static'
STATIC_URL = '/torpedo/static/'
