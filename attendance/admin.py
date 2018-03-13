from django.contrib import admin
from .models import Employee
from .models import Leave_Application
from .models import Attendance

# Register your models here. "attendance"

admin.site.register(Attendance)
admin.site.register(Leave_Application)

