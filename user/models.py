from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from company.models import Company, Designation, Department, JobType
#from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
import decimal

#-----------------------------------------------------------------------------------------------------------------------
class Employee(models.Model):
    '''
       stores all the personal info about employee and its job description
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=50,null=True)
    contact = models.CharField(max_length=15)
    alt_contact = models.CharField(max_length=15,null=True,blank=True)
#    email = models.EmailField()
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
                                    default = 'none/no_profile.png',
                                    null = True,
                                    blank = True
                                   )
    probation_period = models.PositiveSmallIntegerField(default=0)
    is_admin = models.NullBooleanField()
    company_id = models.ForeignKey('company.Company')
    

    def __str__(self):
        return self.name
#-----------------------------------------------------------------------------------------------------------------------
class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(decimal_places = 2,
                                 max_digits = 10,
                                 default = decimal.Decimal('0.0000000000')
                                )
    updation_date = models.DateField()
    effective_from = models.DateField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Salary details on date :  "+str(self.updation_date)
    
#-----------------------------------------------------------------------------------------------------------------------
#code from simpleisbetterthancomplex.com
# @receiver(post_save, sender=User)
# def create_user_employee(sender, instance, created, **kwargs):
#     if created:
#         Employee.objects.create(user=instance)
        
# @receiver(post_save, sender=User)
# def save_user_employee(sender, instance, **kwargs):
#     instance.employee.save()
#-----------------------------------------------------------------------------------------------------------------------
class DesignationHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,null=True)
    date = models.DateField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Designation History details on date :  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------
class DepartmentHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,null=True)
    date = models.DateField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Department History details on date :  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------
class JobTypeHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_type = models.ForeignKey(JobType, null=True)
    date = models.DateField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Job Type History details on date :  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------
class LeaveHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance = models.ForeignKey("attendance.Attendance")
    date = models.DateField()
    privilege_leave = models.PositiveSmallIntegerField()
    casual_leave = models.PositiveSmallIntegerField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Leave History details on date :  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------

