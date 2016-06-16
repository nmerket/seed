# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-14 20:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0017_column_extra_data_source'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='column',
            unique_together=set([('organization', 'column_name', 'is_extra_data', 'extra_data_source')]),
        ),
    ]
