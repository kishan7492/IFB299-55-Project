# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IFB299Project', '0004_auto_20171004_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeinformation',
            name='Placename',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
