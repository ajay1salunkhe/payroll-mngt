# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-17 09:47
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0007_auto_20180423_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('basic_salary_per', models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('basic_amount', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('hra_per', models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('hra_amount', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('conveyance_allow', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('special_allow', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('prof_tax', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('income_tax', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('loss_of_pay', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('gross_earning', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('gross_deduction', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('total_days', models.PositiveSmallIntegerField(default=0)),
                ('weekly_off', models.PositiveSmallIntegerField(default=0)),
                ('public_holidays', models.PositiveSmallIntegerField(default=0)),
                ('paid_days', models.PositiveSmallIntegerField(default=0)),
                ('net_salary', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('basic_salary_per', models.FloatField()),
                ('hra_per', models.FloatField()),
                ('conveyance_allow', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('special_allow', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('prof_tax', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('income_tax', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('loss_of_pay', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('gross_earning', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('gross_deduction', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('total_days', models.PositiveSmallIntegerField(default=0)),
                ('weekly_off', models.PositiveSmallIntegerField(default=0)),
                ('public_holidays', models.PositiveSmallIntegerField(default=0)),
                ('paid_days', models.PositiveSmallIntegerField(default=0)),
                ('net_salary', models.DecimalField(decimal_places=2, default=Decimal('0E-10'), max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Employee')),
                ('salary_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Salary')),
            ],
        ),
    ]
