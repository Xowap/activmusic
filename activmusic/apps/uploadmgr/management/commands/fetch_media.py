# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2015 ActivKonnect

from pprint import pprint
from django.core.files import File
from os import chdir
from shutil import rmtree
from tempfile import mkdtemp
from django.core.management.base import BaseCommand
from django.db.models import Q
from tendo.singleton import SingleInstance
from youtube_dl.YoutubeDL import YoutubeDL
from activmusic.apps.uploadmgr.models import AudioMedia


class MyLogger(object):
    def __init__(self):
        self.has_error = False

    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        self.has_error = True


def hook(d):
    pprint(d)


class Command(BaseCommand):
    def handle(self, *args, **options):
        SingleInstance()

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'vorbis',
                'preferredquality': '0',
            }],
            # 'progress_hooks': [hook],
        }

        dir_name = mkdtemp()

        try:
            chdir(dir_name)

            for media in AudioMedia.objects.filter(Q(file__isnull=True) | Q(file='')):
                self.stdout.write('Downloading {}...'.format(media))

                opts = dict(ydl_opts)
                opts['outtmpl'] = '{}.%(ext)s'.format(media.pk)
                opts['logger'] = MyLogger()
                with YoutubeDL(opts) as ydl:
                    result = ydl.extract_info(media.url)

                    if not opts['logger'].has_error:
                        name = '{}.ogg'.format(media.pk)
                        with open(name, 'rb') as f:
                            media.file.save('{}-{}.ogg'.format(
                                media.pk,
                                result.get('title')
                            ), File(f))
                        media.name = result.get('title')
                        media.save()
        finally:
            rmtree(dir_name)
