from django.contrib import admin
from .models import Employee

from .models import Salary
from .models import Salary_History
'''
from .models import Company
from .models import Holiday
from .models import Work_Type
from .models import Designation
from .models import Designation_History
from .models import Department
from .models import Department_History
from .models import Job_Type
from .models import Job_Type_History
from .models import Leave_History
from .models import Leave_Application
'''
# Register your models here. "payroll" 
'''
admin.site.register(Company)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(Job_Type)
admin.site.register(Work_Type)
admin.site.register(Holiday)
'''
'''
admin.site.register(Employee)
admin.site.register(Attendance)
'''
admin.site.register(Salary)
admin.site.register(Salary_History)
'''
admin.site.register(Designation_History)
admin.site.register(Department_History)
admin.site.register(Job_Type_History)
admin.site.register(Leave_History)
admin.site.register(Leave_Application)
'''
