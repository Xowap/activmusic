# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from django.shortcuts import render


def index(request):
    return render(request, 'base.html')
