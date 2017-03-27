# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20170327_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='settings',
            field=models.ForeignKey(to='todo.Setting', null=True, verbose_name='Paramètres'),
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(to='todo.Member', blank=True, null=True, related_name='tasks_assigned', verbose_name='Assigné à'),
        ),
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(verbose_name='avatar member', upload_to='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='notify_mail',
            field=models.BooleanField(default=True, verbose_name='Notifications par Email ?'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='notify_sms',
            field=models.BooleanField(default=True, verbose_name='Notifications par sms ?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 28, 20, 15, 50, 142587, tzinfo=utc), verbose_name='Fin prévue le', null=True, blank=True),
        ),
    ]
