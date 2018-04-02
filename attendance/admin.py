from django.contrib import admin
from .models import Employee
from .models import LeaveApplication
from .models import Attendance

# Register your models here. "attendance"

admin.site.register(Attendance)
admin.site.register(LeaveApplication)

