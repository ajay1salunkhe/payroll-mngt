from django.db import models
from django.utils import timezone
from datetime import datetime
from user.models import Employee
from django.core.validators import MaxValueValidator, MinValueValidator

import decimal

#this is "payroll" models.py

#-----------------------------------------------------------------------------------------------------------------------
class Salary(models.Model):
    '''
    salary related info of employee like gross,net  salary, allowances and deductions 
    '''
    employee = models.ForeignKey(Employee)
    date = models.DateField()
    basic_salary_perc = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)],default=45)

    hra_perc = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)],default=45)

    conveyance_allow = models.DecimalField(decimal_places = 2,
                                           max_digits = 10,
                                           default = decimal.Decimal('1600.0000000000')
    )

    prof_tax = models.DecimalField(decimal_places = 2,
                                        max_digits = 10,
                                        default = decimal.Decimal('200.0000000000')
    )
    income_tax_perc = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)],default=10)
    gross_month_salary = models.DecimalField(decimal_places = 2,
                                        max_digits = 10,
                                        default = decimal.Decimal('0.0000000000')
    )
    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Salary details on date :  "+str(self.date)
    #-----------------------------------------------------------------------------------------------------------------------
class SalaryHistory(models.Model):
    '''
    salary related info of employee like gross,net  salary, allowances and deductions 
    '''
    employee = models.ForeignKey(Employee)
    date = models.DateField()
    month_year = models.CharField(max_length=10,default="")
    basic_perc = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    basic = models.DecimalField(decimal_places = 2,
                                           max_digits = 10,
                                           default = decimal.Decimal('0.0000000000')
    )
    hra_perc = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    hra = models.DecimalField(decimal_places = 2,
                                           max_digits = 10,
                                           default = decimal.Decimal('0.0000000000')
    )
    conveyance_allow = models.DecimalField(decimal_places = 2,
                                           max_digits = 10,
                                           default = decimal.Decimal('0.0000000000')
    )
    special_allow = models.DecimalField(decimal_places = 2,
                                        max_digits = 10,
                                        default = decimal.Decimal('0.0000000000')
    )
    prof_tax = models.DecimalField(decimal_places = 2,
                                   max_digits = 10,
                                   default = decimal.Decimal('0.0000000000')
    )
    income_tax_perc = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)],default=0)
    income_tax = models.DecimalField(decimal_places = 2,
                                     max_digits = 10,
                                     default = decimal.Decimal('0.0000000000')
    )
    loss_of_pay = models.DecimalField(decimal_places = 2,
                                      max_digits = 10,
                                      default = decimal.Decimal('0.0000000000')
    )
    gross_earning = models.DecimalField(decimal_places = 2,
                                        max_digits = 10,
                                        default = decimal.Decimal('0.0000000000')
    )
    gross_deduction = models.DecimalField(decimal_places = 2,
                                          max_digits = 10,
                                          default = decimal.Decimal('0.0000000000')
    )
    working_days = models.PositiveSmallIntegerField(default=0)
    paid_days = models.PositiveSmallIntegerField(default=0)
    leaves = models.PositiveSmallIntegerField(default=0)
    lop_days = models.PositiveSmallIntegerField(default=0)
    net_salary = models.DecimalField(decimal_places = 2,
                                     max_digits = 10,
                                     default = decimal.Decimal('0.0000000000')
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Salary History details on date :  "+str(self.date)
    #-----------------------------------------------------------------------------------------------------------------------
