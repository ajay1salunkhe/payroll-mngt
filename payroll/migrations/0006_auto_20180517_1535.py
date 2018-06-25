# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-17 10:05
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0005_auto_20180517_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='basic_salary_perc',
            field=models.FloatField(default=45, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='salary',
            name='conveyance_allow',
            field=models.DecimalField(decimal_places=2, default=Decimal('1600.0000000000'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='salary',
            name='hra_perc',
            field=models.FloatField(default=45, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='salary',
            name='prof_tax',
            field=models.DecimalField(decimal_places=2, default=Decimal('200.0000000000'), max_digits=10),
        ),
    ]