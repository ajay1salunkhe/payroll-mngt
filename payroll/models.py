from django.db import models
from django.utils import timezone
from datetime import datetime
from user.models import Employee

import decimal

#this is "payroll" models.py

#-----------------------------------------------------------------------------------------------------------------------
class Salary(models.Model):
    '''
    salary related info of employee like gross,net  salary, allowances and deductions 
    '''
    employee = models.ForeignKey(Employee)
    date = models.DateField()
    basic_salary_per = models.FloatField()
    hra_per = models.FloatField()
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
    total_days = models.PositiveSmallIntegerField(default=0)
    weekly_off = models.PositiveSmallIntegerField(default=0)
    public_holidays = models.PositiveSmallIntegerField(default=0)
    paid_days = models.PositiveSmallIntegerField(default=0)
    net_salary = models.DecimalField(decimal_places = 2,
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
    salary_id = models.ForeignKey("payroll.Salary")
    date = models.DateField()
    basic_salary_per = models.FloatField()
    hra_per = models.FloatField()
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
    total_days = models.PositiveSmallIntegerField(default=0)
    weekly_off = models.PositiveSmallIntegerField(default=0)
    public_holidays = models.PositiveSmallIntegerField(default=0)
    paid_days = models.PositiveSmallIntegerField(default=0)
    net_salary = models.DecimalField(decimal_places = 2,
                                     max_digits = 10,
                                     default = decimal.Decimal('0.0000000000')
                                    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Salary History details on date :  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------
