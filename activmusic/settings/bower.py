# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from .utils import *

BOWER_COMPONENTS_ROOT = DJANGO_ROOT.child('components')

BOWER_INSTALLED_APPS = (
    'angular#~1.3',
    'angular-animate#~1.3',
    'angular-cookies#~1.3',
    'bootstrap#~3.2',
    'lesshat#~3.0',
)
