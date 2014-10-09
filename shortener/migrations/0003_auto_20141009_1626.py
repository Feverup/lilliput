# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20141009_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='hash',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name=' URL Hash', blank=True),
        ),
    ]
