# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-17 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0006_auto_20180517_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='special_allow',
        ),
    ]
