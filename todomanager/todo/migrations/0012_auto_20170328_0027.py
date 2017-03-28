# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20170327_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='Fin prévue le', null=True, blank=True, default=datetime.datetime(2017, 3, 29, 0, 27, 47, 670681, tzinfo=utc)),
        ),
    ]
