# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-14 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180314_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(default='none/no_profile.png', upload_to='user_profiles/'),
        ),
    ]
