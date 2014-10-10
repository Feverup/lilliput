# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20141009_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='original_url',
            field=models.URLField(unique=True, max_length=2000, verbose_name='Original URL'),
        ),
    ]
