# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='utilisateur', related_name='todo_member_user')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Crée le')),
                ('modified_at', models.DateTimeField(verbose_name='Modifié le', auto_now=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=60)),
                ('description', models.TextField(verbose_name='Description', null=True, blank=True)),
                ('due_date', models.DateTimeField(verbose_name='Fin prévue le', default=datetime.datetime(2017, 3, 28, 18, 27, 37, 200730, tzinfo=utc), null=True, blank=True)),
                ('completed', models.BooleanField(verbose_name='Tache terminée ? ', default=False)),
                ('status', models.CharField(default=None, choices=[(None, '---')], max_length=20, null=True, blank=True)),
                ('created_by', models.ForeignKey(verbose_name='Crée par', to='todo.Member', related_name='todo_task_modificator')),
                ('modified_by', models.ForeignKey(verbose_name='Modifié par', to='todo.Member', related_name='todo_task_creator')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
