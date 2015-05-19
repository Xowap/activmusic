# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect


from django.contrib import admin
from activmusic.apps.uploadmgr.models import AudioMedia, Playlist


@admin.register(AudioMedia)
class AudioMediaAdmin(admin.ModelAdmin):
    list_display = ('url', 'owner', 'name', 'failed')
    list_filter = ('failed',)
    search_fields = ('url', 'owner__first_name', 'owner__last_name', 'name')


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {
        'slug': ('name',),
    }
