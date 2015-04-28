# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'activmusic.apps.uploadmgr.views',

    url(r'^$', 'music_list', name='music_list'),
    url(r'^add/$', 'music_add', name='music_add'),
)
