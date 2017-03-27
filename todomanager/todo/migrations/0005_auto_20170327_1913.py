# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20170327_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('modified_at', models.DateTimeField(verbose_name='Modifié le', auto_now=True)),
                ('notify_mail', models.BooleanField(verbose_name='')),
                ('notify_sms', models.BooleanField(verbose_name='')),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(verbose_name='utilisateur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 28, 19, 13, 55, 287631, tzinfo=utc), null=True, verbose_name='Fin prévue le'),
        ),
        migrations.AddField(
            model_name='setting',
            name='created_by',
            field=models.ForeignKey(verbose_name='Crée par', to='todo.Member', related_name='todo_setting_modificator'),
        ),
        migrations.AddField(
            model_name='setting',
            name='modified_by',
            field=models.ForeignKey(verbose_name='Modifié par', to='todo.Member', related_name='todo_setting_creator'),
        ),
    ]
