# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-22 10:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0007_remove_salary_special_allow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salaryhistory',
            name='public_holidays',
        ),
        migrations.RemoveField(
            model_name='salaryhistory',
            name='salary_id',
        ),
        migrations.RemoveField(
            model_name='salaryhistory',
            name='weekly_off',
        ),
    ]
