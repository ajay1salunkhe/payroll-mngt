# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-10 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_auto_20180425_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='lop',
            field=models.BooleanField(default=False),
        ),
    ]