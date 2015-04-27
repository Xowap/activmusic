#!/usr/bin/env python
# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "activmusic.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
