from django.db import models
from django.utils import timezone
from datetime import datetime
from user.models import Employee
from company.models import WorkType

#this is "attendance" models.py

#-----------------------------------------------------------------------------------------------------------------------
class Attendance(models.Model):
    employee = models.ForeignKey(Employee)
    work_type = models.ForeignKey(WorkType)
    date = models.DateField()
    mark_choices = (
        (0,'Absent'),
        (0.5,'Half day'),
        (1,'Present')
    )
    mark = models.FloatField(choices=mark_choices)        
    rem_privilege_leave = models.PositiveSmallIntegerField(default=0)
    rem_casual_leave = models.PositiveSmallIntegerField(default=0)
    leave_type = models.CharField(max_length = 20,
                                  default='---'
                                 )
    
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's attendance details on  "+str(self.date)
#-----------------------------------------------------------------------------------------------------------------------
class LeaveApplication(models.Model):
    employee = models.ForeignKey(Employee)
    leave_from = models.DateField()
    leave_to = models.DateField()
    leave_type = models.CharField(max_length = 20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.employee.name+" 's Leave Application details on date :  "+str(self.leave_from)
#-----------------------------------------------------------------------------------------------------------------------
