# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-25 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20180425_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='leave_type',
            field=models.CharField(blank=True, choices=[('PL', 'Privilege Leave'), ('CL', 'Casual Leave')], max_length=20, null=True),
        ),
    ]
