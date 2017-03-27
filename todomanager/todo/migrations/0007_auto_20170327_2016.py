# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20170327_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='settings',
            field=models.ForeignKey(to='todo.Setting', verbose_name='Paramètres', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fin prévue le', default=datetime.datetime(2017, 3, 28, 20, 16, 58, 70353, tzinfo=utc)),
        ),
    ]
