# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_auto_20170328_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 29, 1, 42, 14, 684116, tzinfo=utc), null=True, verbose_name='Fin prévue le', blank=True),
        ),
    ]
