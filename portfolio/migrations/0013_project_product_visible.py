# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_project_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='product_visible',
            field=models.BooleanField(default=False),
        ),
    ]
