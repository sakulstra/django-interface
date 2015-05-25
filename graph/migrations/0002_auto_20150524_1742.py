# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordata',
            old_name='server_date',
            new_name='created',
        ),
        migrations.AddField(
            model_name='sensordata',
            name='annual_precipitation',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='power',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='temperature',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='wind_direction',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='wind_speed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
