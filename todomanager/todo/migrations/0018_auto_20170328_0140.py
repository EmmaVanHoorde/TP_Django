# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0017_auto_20170328_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fin prévue le', default=datetime.datetime(2017, 3, 29, 1, 40, 59, 2602, tzinfo=utc)),
        ),
    ]
