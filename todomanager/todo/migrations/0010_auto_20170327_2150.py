# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20170327_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, verbose_name='Fin prévue le', null=True, default=datetime.datetime(2017, 3, 28, 21, 50, 35, 619390, tzinfo=utc)),
        ),
    ]
