from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=50,null=True)
    contact = models.CharField(max_length=15)
    alt_contact = models.CharField(max_length=15,null=True)
    email = models.EmailField()
    gender_choices = (('M','Male'),('F','Female'))
    gender = models.CharField(max_length=2,choices=gender_choices)
    dob = models.DateField()
    pan_id = models.CharField(max_length=15,null=True)
    aadhar_no = models.CharField(max_length=15)
    profile_pic = models.BinaryField()
    tax_status_choices = (("nri","NRI"),("resident","RESIDENT"),("expat","EXPAT"))
    tax_status = models.CharField(max_length=10,choices=tax_status_choices)
    total_leave = models.PositiveSmallIntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee)
    date = models.DateField(null=True)
    mark_choices = ((0,'Absent'),(0.5,'Half day'),(1,'Present'))
    mark = models.IntegerField(choices=mark_choices)
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

#class JobDescription(models.Model):
    
