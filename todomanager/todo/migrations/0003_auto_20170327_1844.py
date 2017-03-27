# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20170327_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 28, 18, 44, 15, 622191, tzinfo=utc), null=True, blank=True, verbose_name='Fin prévue le'),
        ),
    ]
