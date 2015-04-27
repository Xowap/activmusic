# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect


from django.contrib import admin
from activmusic.apps.uploadmgr.models import AudioMedia


@admin.register(AudioMedia)
class AudioMediaAdmin(admin.ModelAdmin):
    list_display = ('url', 'owner', 'name')
