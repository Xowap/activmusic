# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns(
    'activmusic.apps.register.views',

    url('^test/$', 'index', name='accounts_test'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
