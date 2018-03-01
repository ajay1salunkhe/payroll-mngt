from django.db import models
from django.utils import timezone


class Employee(models.Model):
    emp_id = models.AutoField('auth.User', primary_key=True)
    emp_name = models.CharField(max_length=30)
    emp_address = models.TextField(max_length=50)
    emp_contact = models.CharField(max_length=15)
    emp_alt_contact = models.CharField(max_length=15)
    emp_email = models.EmailField()
    gender_choices = (('M','Male'),('F','Female'))
    emp_gender = models.CharField(max_length=7,choices=gender_choices)
    emp_dob = models.dateTimeField()
    emp_pan_id = models.models.CharField(max_length=15)
    emp_aadhar_no = models.models.CharField(max_length=15)
    emp_profile_pic = models.models.BinaryField()
    tax_status = ((NRI,NRI),(RESIDENT,RESIDENT),(EXPAT,EXPAT))
    emp_tax_status = models.CharField(max_length=10,choices=tax_status)
    emp_total_leave = models.PositiveSmallIntegerField() 

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Attendance(models.Model):
