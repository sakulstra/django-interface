# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_auto_20150524_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordata',
            old_name='annual_precipitation',
            new_name='precipitation',
        ),
    ]
