# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "activmusic.settings.prod")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
