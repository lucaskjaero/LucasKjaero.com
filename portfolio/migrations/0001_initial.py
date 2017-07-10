# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('difficulty', models.IntegerField()),
                ('source_open', models.BooleanField(default=True)),
                ('source_available', models.BooleanField(default=True)),
                ('view_link', models.CharField(blank=True, max_length=300)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='portfolio.Technology'),
        ),
    ]