
from django.db import models
from django.utils import timezone
from datetime import datetime
import decimal

#this is "company" models.py

#-----------------------------------------------------------------------------------------------------------------------
class Company(models.Model):
    namec = models.CharField(max_length = 50)
    address = models.TextField(max_length = 150)
    #address_line2 = models.TextField(max_length = 50)
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
        return self.namec
#-----------------------------------------------------------------------------------------------------------------------
class Holiday(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length = 50)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.company.namec+" job Holiday on date  "+str(datetime.now())
#-----------------------------------------------------------------------------------------------------------------------
class WorkType(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    wt_choices = (('SunHol','Sunday Holiday'),
                      ('SatSunHol','Sat-Sun Holiday')
                     )
    work_type = models.CharField(max_length = 20, choices = wt_choices)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.work_type
#-----------------------------------------------------------------------------------------------------------------------
class Designation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
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
        return self.designation
#-----------------------------------------------------------------------------------------------------------------------
class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.CharField(max_length = 20)
    
    def publish(self):
        self.save()
    def __str__(self):
        return self.department
#-----------------------------------------------------------------------------------------------------------------------
class JobType(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type = models.CharField(max_length = 20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.job_type
#-----------------------------------------------------------------------------------------------------------------------
