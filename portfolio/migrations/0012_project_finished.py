# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20170710_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='finished',
            field=models.BooleanField(default=True),
        ),
    ]
