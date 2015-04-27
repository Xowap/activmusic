# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from .common import *
from os import getenv

ALLOWED_HOSTS = ['*']

DEFAULT_FILE_STORAGE = 'activmusic.lib.storage.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = getenv('AWS_S3_CUSTOM_DOMAIN')
AWS_S3_URL_PROTOCOL = 'https:'

AWS_HEADERS = {
    'Expires': 'Thu, 1 Jan 2030 20:00:00 GMT',
    'Cache-Control': 'max-age=315360000',
}

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
