# Development settings file
#

import os
CURDIR = os.path.dirname(__file__)
execfile(os.path.join(CURDIR, 'settings.py'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
MAILER_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PIPELINE_CSS = {
    'torpedo': {
        'source_filenames': (
          os.path.join('stylesheets','less','*.less'),
        ),
    },
}
