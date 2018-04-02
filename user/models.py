from django.db import models
from django.utils import timezone
from datetime import datetime
from company.models import Company
#from attendance.models import Attendance

#this is "user" models.py

#-----------------------------------------------------------------------------------------------------------------------
class Employee(models.Model):
    '''
       stores all the personal info about employee and its job description
    '''
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=50,null=True)
    contact = models.CharField(max_length=15)
    alt_contact = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField()
    gender_choices = (('M','Male'),
                      ('F','Female')
                     )
    gender = models.CharField(max_length = 2,
                              choices = gender_choices
                             )
    dob = models.DateField()
    pan_id = models.CharField(max_length = 15,
                              null = True,
                              blank = True
                             )
    aadhar_no = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to = 'user_profiles/',
                                    default = 'none/no_profile.png'
                                   )
    probation_period = models.PositiveSmallIntegerField(default=0)
    company_id = models.ForeignKey('company.Company')
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name
#-----------------------------------------------------------------------------------------------------------------------
class DesignationHistory(models.Model):
    employee = models.ForeignKey(Employee)
    designation_id = models.ForeignKey(Company)
    date = models.DateField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Designation History details on date :  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------
class DepartmentHistory(models.Model):
    employee = models.ForeignKey(Employee)
    department_id = models.ForeignKey(Company)
    date = models.DateField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Department History details on date :  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------
class JobTypeHistory(models.Model):
    employee = models.ForeignKey(Employee)
    job_type_id = models.ForeignKey(Company)
    date = models.DateField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Job Type History details on date :  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------
class LeaveHistory(models.Model):
    employee = models.ForeignKey(Employee)
    attendance_id = models.ForeignKey("attendance.Attendance")
    date = models.DateField()
    privilege_leave = models.PositiveSmallIntegerField()
    casual_leave = models.PositiveSmallIntegerField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Leave History details on date :  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------

