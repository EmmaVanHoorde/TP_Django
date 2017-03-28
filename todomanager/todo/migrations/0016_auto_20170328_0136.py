# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0015_auto_20170328_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='Fin prévue le', default=datetime.datetime(2017, 3, 29, 1, 36, 10, 588829, tzinfo=utc), blank=True),
        ),
    ]
