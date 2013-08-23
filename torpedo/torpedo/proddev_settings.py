# Development settings file
#

import os
CURDIR = os.path.dirname(__file__)
execfile(os.path.join(CURDIR, 'settings.py'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'torpedo',                      # Or path to database file if using sqlite3.
        'USER': 'teerytko_nt',                      # Not used with sqlite3.
        'PASSWORD': 'torpedo',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SERVE_MEDIA = True
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'torpedo/media')
#MEDIA_URL = 'http://nokiantorpedo.fi/torpedo/media/'
MEDIA_URL = '/media/'
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
