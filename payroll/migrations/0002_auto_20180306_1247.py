# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('basic_salary_per', models.FloatField()),
                ('hra_per', models.FloatField()),
                ('conveyance_allow', models.PositiveIntegerField()),
                ('special_allow', models.PositiveIntegerField()),
                ('prof_tax', models.PositiveIntegerField()),
                ('income_tax', models.PositiveIntegerField()),
                ('loss_of_pay', models.PositiveIntegerField()),
                ('gross_salary', models.PositiveIntegerField()),
                ('net_salary', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='tax_status',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='total_leave',
        ),
        migrations.AddField(
            model_name='attendance',
            name='total_leave',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='bank_acc_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='job_type',
            field=models.CharField(choices=[('intern', 'Intern'), ('working', 'Working')], default='none', max_length=15),
        ),
        migrations.AddField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='payment_mode',
            field=models.CharField(choices=[('paycheck', 'Paycheck'), ('direct deposit', 'Direct deposit'), ('cash', 'Cash')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='alt_contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pan_id',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='salary',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Employee'),
        ),
    ]