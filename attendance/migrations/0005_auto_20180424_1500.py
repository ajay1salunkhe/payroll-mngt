# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-24 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20180424_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='leave_type',
            field=models.CharField(choices=[('Privilege Leave', 'Privilege Leave'), ('Casual Leave', 'Casual Leave')], max_length=20),
        ),
    ]
