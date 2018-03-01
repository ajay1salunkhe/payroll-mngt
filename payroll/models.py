from django.db import models
from django.utils import timezone


class Employee(models.Model):
    emp_id = models.AutoField('auth.User', primary_key=True)
    emp_name = models.CharField(max_length=30)
    emp_address = models.TextField(max_length=50)
    def publish(self):
        self.save()

    def __str__(self):
        return self.title
