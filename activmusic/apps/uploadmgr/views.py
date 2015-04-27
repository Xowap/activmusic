# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from django.http.response import HttpResponse
from random import shuffle
from activmusic.apps.uploadmgr.models import AudioMedia


def playlist(request, slug):
    output = ["#EXTM3U"]

    medias = list(AudioMedia.objects.filter(owner__playlist__slug=slug)
                  .exclude(file__isnull=True)
                  .exclude(file=''))
    shuffle(medias)

    output += ['#EXTINF:{},{}\r\n{}'.format(x.duration,
                                            x.name,
                                            request.build_absolute_uri(x.file.url))
               for x in medias]

    return HttpResponse('\r\n'.join(output).encode('utf-8'), content_type='application/x-mpegurl')
