from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=50,null=True)
    contact = models.CharField(max_length=15)
    alt_contact = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField()
    gender_choices = (('M','Male'),('F','Female'))
    gender = models.CharField(max_length=2,choices=gender_choices)
    dob = models.DateField()
    pan_id = models.CharField(max_length=15,null=True,blank=True)
    aadhar_no = models.CharField(max_length=15)
    profile_pic = models.BinaryField()
#    tax_status_choices = (("nri","NRI"),("resident","RESIDENT"),("expat","EXPAT"))
#    tax_status = models.CharField(max_length=10,choices=tax_status_choices)
    joining_date = models.DateField(null=True)
    job_types = (("intern","Intern"),("working","Working"))
    job_type = models.CharField(max_length=15,choices=job_types,default="none")
    payment_modes = (("paycheck","Paycheck"),("direct deposit","Direct deposit"),("cash","Cash"))
    payment_mode = models.CharField(max_length=15,choices=payment_modes,null=True)
    bank_acc_no = models.CharField(max_length=15,null=True,blank=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee)
    date = models.DateField(null=True)
    mark_choices = ((0,'Absent'),(0.5,'Half day'),(1,'Present'))
    mark = models.IntegerField(choices=mark_choices)
    total_leave = models.PositiveSmallIntegerField(default=0)
    
    def publish(self):
        self.save()

class Salary(models.Model):
    employee = models.ForeignKey(Employee)
    amount = models.PositiveIntegerField()
    basic_salary_per = models.FloatField()
    hra_per = models.FloatField()
    conveyance_allow = models.PositiveIntegerField()
    special_allow = models.PositiveIntegerField()
    prof_tax = models.PositiveIntegerField()
    income_tax = models.PositiveIntegerField()
    loss_of_pay = models.PositiveIntegerField()
    gross_salary = models.PositiveIntegerField()
    net_salary = models.PositiveIntegerField()

    def publish(self):
        self.save()
    
