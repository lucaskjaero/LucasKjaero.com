# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20170709_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='icon',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='technology',
            name='link',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
