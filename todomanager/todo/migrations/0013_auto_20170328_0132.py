# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_auto_20170328_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 29, 1, 32, 8, 494493, tzinfo=utc), null=True, blank=True, verbose_name='Fin prévue le'),
        ),
    ]
