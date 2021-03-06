# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-24 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20180424_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='leave_type',
            field=models.CharField(choices=[(1, 'Privilege Leave'), (2, 'Casual Leave')], max_length=20),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='work_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.WorkType'),
        ),
    ]
