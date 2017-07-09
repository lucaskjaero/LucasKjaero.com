# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20151027_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default='http://www.angelafloydschools.com/wp-content/uploads/placeholder-car1.png', max_length=300),
        ),
    ]
