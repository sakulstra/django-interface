# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0003_auto_20150525_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='gsm_timestamp',
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
