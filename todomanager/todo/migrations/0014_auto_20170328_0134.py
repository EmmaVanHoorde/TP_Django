# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_auto_20170328_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='Fin prévue le', blank=True, default=datetime.datetime(2017, 3, 29, 1, 34, 23, 103483, tzinfo=utc), null=True),
        ),
    ]
