# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0010_auto_20160115_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_client',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_manager',
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(choices=[('CL', 'Client'), ('MG', 'Manager'), ('TR', 'Translator')], default='TR', max_length=2),
        ),
    ]
