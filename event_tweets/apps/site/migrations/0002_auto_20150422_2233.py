# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='max_id_checked',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='min_id_checked',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
