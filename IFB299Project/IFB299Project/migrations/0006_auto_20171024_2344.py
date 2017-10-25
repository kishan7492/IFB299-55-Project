# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IFB299Project', '0005_auto_20171024_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='userID',
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
