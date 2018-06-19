from django.contrib import admin
from .models import Employee
from .models import DesignationHistory
from .models import DepartmentHistory
from .models import JobTypeHistory
from .models import LeaveHistory
from .models import EmployeeSalary
# Register your models here. "user"

admin.site.register(Employee)
admin.site.register(DesignationHistory)
admin.site.register(DepartmentHistory)
admin.site.register(JobTypeHistory)
admin.site.register(LeaveHistory)
admin.site.register(EmployeeSalary)


