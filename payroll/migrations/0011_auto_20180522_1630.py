# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-22 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0010_auto_20180522_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salaryhistory',
            old_name='total_days',
            new_name='working_days',
        ),
    ]
