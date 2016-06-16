# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-14 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0016_auto_20160411_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='extra_data_source',
            field=models.CharField(blank=True, choices=[(b'P', b'Property'), (b'T', b'Taxlot')], db_index=True, max_length=1, null=True),
        ),
    ]
