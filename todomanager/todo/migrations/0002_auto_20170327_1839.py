# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 28, 18, 39, 24, 927581, tzinfo=utc), null=True, verbose_name='Fin prévue le'),
        ),
    ]
