# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from random import shuffle
from django.shortcuts import render, redirect
from activmusic.apps.uploadmgr.forms import AudioMediaForm
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


@login_required
def music_list(request):
    return render(request, 'uploadmgr/index.html', {
        'medias': AudioMedia.objects.filter(owner=request.user)
    })


@login_required
def music_add(request):
    if request.method == 'POST':
        form = AudioMediaForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            return redirect('music_list')
    else:
        form = AudioMediaForm(request.user)

    return render(request, 'uploadmgr/add.html', {
        'form': form
    })
