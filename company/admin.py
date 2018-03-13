from django.contrib import admin
from .models import Company
from .models import Holiday
from .models import Work_Type
from .models import Designation
from .models import Department
from .models import Job_Type

# Register your models here. "company"

admin.site.register(Company)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(Job_Type)
admin.site.register(Work_Type)
admin.site.register(Holiday)
