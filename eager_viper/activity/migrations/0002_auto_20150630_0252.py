# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 6, 30, 2, 52, 12, 293851, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stat',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 6, 30, 2, 52, 12, 293851, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stat',
            name='activity',
            field=models.ForeignKey(to='activity.Activity', related_name='stats'),
        ),
    ]
