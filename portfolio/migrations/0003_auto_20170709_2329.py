# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20170709_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='link',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AddField(
            model_name='technology',
            name='slug',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
