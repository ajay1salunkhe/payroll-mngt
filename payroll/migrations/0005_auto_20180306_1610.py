# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0004_auto_20180306_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='no_of_leaves',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='no_of_present_days',
        ),
    ]
