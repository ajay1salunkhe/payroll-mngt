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
    emp_dob = models.DateField()
    emp_pan_id = models.CharField(max_length=15)
    emp_aadhar_no = models.CharField(max_length=15)
    emp_profile_pic = models.BinaryField()
    tax_status = (("nri","NRI"),("resident","RESIDENT"),("expat","EXPAT"))
    emp_tax_status = models.CharField(max_length=10,choices=tax_status)
    emp_total_leave = models.PositiveSmallIntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.emp_name

class Attendance(models.Model):
    att_date = models.DateField()
    mark_choices = ((0,'Absent'),(0.5,'Half day'),(1,'Present'))
    att_mark = models.IntegerField(max_length=3,choices=mark_choices)
    is_half_day = False
    def publish(self):
        if mark_choices==0:
            leave_type="Absent"
        elif mark_choices==1:
            leave_type="Present"
        elif mark_choices==0.5:
            leave_type="Half Day"
            is_half_day=True
        self.save()
