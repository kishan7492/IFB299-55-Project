# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IFB299Project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pageee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IFB299Project.Category')),
            ],
        ),
    ]
