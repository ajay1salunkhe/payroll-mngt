from django.db import models
from django.utils import timezone
from datetime import datetime
import decimal

#this is "company" models.py

#-----------------------------------------------------------------------------------------------------------------------
class Company(models.Model):
    name = models.CharField(max_length = 50)
    address_line1 = models.TextField(max_length = 50)
    address_line2 = models.TextField(max_length = 50)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    postal_code = models.PositiveIntegerField()
    fax = models.CharField(max_length = 20,
                           null = True,
                           blank=True
                          )
    website = models.CharField(max_length = 50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
#-----------------------------------------------------------------------------------------------------------------------
class Holiday(models.Model):
    company = models.ForeignKey(Company)
    date = models.DateField()
    name = models.CharField(max_length = 50)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.company.name+" job Holiday on date  "+str(datetime.now())
#-----------------------------------------------------------------------------------------------------------------------
class WorkType(models.Model):
    company = models.ForeignKey(Company)
    work_type = models.CharField(max_length = 20)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.company.name+" work types"
#-----------------------------------------------------------------------------------------------------------------------
class Designation(models.Model):
    company = models.ForeignKey(Company)
    designation = models.CharField(max_length = 50)
    privilege_leave = models.PositiveSmallIntegerField()
    casual_leave = models.PositiveSmallIntegerField()
    salary = models.DecimalField(decimal_places = 2,
                                 max_digits = 10,
                                 default = decimal.Decimal('0.0000000000')
                                )
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.company.name+" designations"
#-----------------------------------------------------------------------------------------------------------------------
class Department(models.Model):
    company = models.ForeignKey(Company)
    department = models.CharField(max_length = 20)
    
    def publish(self):
        self.save()
    def __str__(self):
        return self.company.name+" departments"
#-----------------------------------------------------------------------------------------------------------------------
class JobType(models.Model):
    company = models.ForeignKey(Company)
    job_type = models.CharField(max_length = 20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.company.name+" job types"
#-----------------------------------------------------------------------------------------------------------------------
