# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadmgr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiomedia',
            name='duration',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
