# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-03 03:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20171102_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='created_date',
            new_name='begining_date',
        ),
        migrations.RenameField(
            model_name='mentor',
            old_name='end_date',
            new_name='ending_date',
        ),
    ]
