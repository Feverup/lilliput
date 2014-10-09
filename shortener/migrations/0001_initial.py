# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_url', models.URLField(verbose_name='Original URL')),
                ('hash', models.CharField(max_length=50, null=True, verbose_name=' URL Hash', db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ShortLink',
                'verbose_name_plural': 'ShortLinks',
            },
            bases=(models.Model,),
        ),
    ]
