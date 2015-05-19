# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from django.db import models
from django.conf import settings
from uuid_upload_path import upload_to


class AudioMedia(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    url = models.URLField()
    name = models.CharField(max_length=1000, null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to=upload_to)
    duration = models.IntegerField(null=True, blank=True)
    failed = models.BooleanField(default=False)

    def __str__(self):
        return self.name if self.name is not None and self.name != '' else self.url


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
