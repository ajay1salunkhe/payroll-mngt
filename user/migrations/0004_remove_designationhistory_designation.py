# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-19 10:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180419_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designationhistory',
            name='designation',
        ),
    ]