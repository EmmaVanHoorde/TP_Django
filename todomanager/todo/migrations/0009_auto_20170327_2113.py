# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20170327_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modifié le')),
                ('name', models.CharField(max_length=60, verbose_name='')),
                ('created_by', models.ForeignKey(verbose_name='Crée par', to='todo.Member', related_name='todo_group_modificator')),
                ('modified_by', models.ForeignKey(verbose_name='Modifié par', to='todo.Member', related_name='todo_group_creator')),
                ('settings', models.ForeignKey(verbose_name='', to='todo.Setting')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('type', models.CharField(max_length=60, verbose_name='')),
                ('group', models.ForeignKey(verbose_name='Relations', to='todo.Group')),
                ('member', models.ForeignKey(verbose_name='', to='todo.Member')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='Fin prévue le', default=datetime.datetime(2017, 3, 28, 21, 13, 44, 320395, tzinfo=utc), blank=True),
        ),
    ]
