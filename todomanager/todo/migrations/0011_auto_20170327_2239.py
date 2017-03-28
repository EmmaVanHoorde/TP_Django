# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20170327_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, verbose_name='Fin prévue le', default=datetime.datetime(2017, 3, 28, 22, 39, 28, 472423, tzinfo=utc), null=True),
        ),
    ]
