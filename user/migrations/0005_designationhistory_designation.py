# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-19 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180418_1004'),
        ('user', '0004_remove_designationhistory_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='designationhistory',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Designation'),
        ),
    ]
