# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-23 05:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_designationhistory_designation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departmenthistory',
            old_name='department_id',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='jobtypehistory',
            old_name='job_type_id',
            new_name='job_type',
        ),
        migrations.RenameField(
            model_name='leavehistory',
            old_name='attendance_id',
            new_name='attendance',
        ),
    ]
