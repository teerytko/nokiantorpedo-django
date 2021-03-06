# Django settings for torpedo project.

import os
SETTINGS_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.join(SETTINGS_ROOT, '../..')
# The base dir
BASEDIR = os.path.join(PROJECT_ROOT, '../..')


DEBUG = True
SERVE_MEDIA = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('admin', 'admin@nokiantorpedo.fi'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Helsinki'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fi'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/teerytko/webapps/torpedo_static/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/torpedo/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/teerytko/webapps/torpedo_static/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/torpedo/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')+p+x#52b25!fe^znraw6!%w3f5djk0hf5g7*10)0(%w+x-psf'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'djangobb_forum.middleware.LastLoginMiddleware',
    'djangobb_forum.middleware.UsersOnline',
)


ROOT_URLCONF = 'torpedo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'torpedo.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'captchacomments',
      # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'djangorestframework',
    'torpedo_main',
    'statistics',
    'registration',
    'pagination',
    'django_authopenid',
    'djangobb_forum',
    #'messages',
    'pipeline',
    'feedjack',
    'events',
    'south',
    'captcha',
    'customflatpages',
    'tagging',
    'mptt',
    'zinnia',
)

COMMENTS_APP = 'captchacomments'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    import mailer
    INSTALLED_APPS += ('mailer',)
    EMAIL_BACKEND = "mailer.backend.DbBackend"
    MAILER_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
except ImportError:
    pass

try:
    import south
    INSTALLED_APPS += ('south',)
    SOUTH_TESTS_MIGRATE = False
except ImportError:
    pass

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django_authopenid.context_processors.authopenid',
    #'django_messages.context_processors.inbox',
    'djangobb_forum.context_processors.forum_settings',
    'torpedo_main.context_processors.load_menu'
)

# Pipeline configuration
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

# Haystack settings
# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'djangobb_index'),
        'INCLUDE_SPELLING': True,
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

DJANGOBB_FORUM_BASE_TITLE = 'Nokian Torpedo Forum'
DJANGOBB_HEADER = 'Nokian Torpedo Forum'
DJANGOBB_TAGLINE = 'Nokialaisen urheiluseuran keskustelu foorumi'

# EMAIL settings
DEFAULT_FROM_EMAIL = 'webmaster@nokiantorpedo.fi'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_SUBJECT_PREFIX = '[NokianTorpedo] '
EMAIL_HOST_USER = 'torpedo'
EMAIL_HOST_PASSWORD = 'admin'
EMAIL_PORT = 587

# Account settings
LOGIN_REDIRECT_URL = '/'
ACCOUNT_ACTIVATION_DAYS = 10
LOGIN_URL = '/forum/account/signin/'
AUTH_PROFILE_MODULE = "torpedo_main.UserProfile"


try:
    from local_settings import *
except ImportError:
    pass
