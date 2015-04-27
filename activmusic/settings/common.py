# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from os import getenv

import dj_database_url

from .utils import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

SITE_ID = 1

INSTALLED_APPS = (
    # Base Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Helper apps
    'raven.contrib.django.raven_compat',
    'djangobower',
    'pipeline',
    'crispy_forms',

    # Our apps
    'activmusic.apps.register',
    'activmusic.apps.uploadmgr',

    # Django Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # General processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    # Django Allauth specific
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'activmusic.urls'

WSGI_APPLICATION = 'activmusic.wsgi.application'


# Database
DATABASES = {
    'default': dj_database_url.config(),
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = DJANGO_ROOT.child('assets')

STATICFILES_DIRS = (
    DJANGO_ROOT.child('static'),
)

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = DJANGO_ROOT.child('media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Templates
TEMPLATE_DIRS = (
    DJANGO_ROOT.child('templates'),
)

# Get SECRET_KEY from env
SECRET_KEY = getenv('SECRET_KEY')

# Email sending
DEFAULT_FROM_EMAIL = 'EMAIL-SENDER@EXAMPLE.COM'
SERVER_EMAIL = 'no-reply@aksrv.net'

# Analytics
METRON_SETTINGS = {
    "google": {
        1: getenv('GOOGLE_ANALYTICS_UID', ''),
    }
}

# Forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Other common config files
from .bower import *
from .pipeline import *
from .auth import *
