# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-25 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_auto_20180425_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='leave_type',
            field=models.CharField(blank=True, choices=[('Privilege Leave', 'Privilege Leave'), ('Casual Leave', 'Casual Leave')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='work_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.WorkType'),
        ),
    ]
