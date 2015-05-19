# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadmgr', '0003_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiomedia',
            name='failed',
            field=models.BooleanField(default=False),
        ),
    ]
