# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20170327_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='avatar',
            field=models.ImageField(upload_to='', null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 28, 18, 48, 39, 769851, tzinfo=utc), null=True, verbose_name='Fin prévue le'),
        ),
    ]
