from django.contrib import admin
from .models import Salary
from .models import SalaryHistory

# Register your models here. "payroll" 

admin.site.register(Salary)
admin.site.register(SalaryHistory)
