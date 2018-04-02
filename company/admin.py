from django.contrib import admin
from .models import Company
from .models import Holiday
from .models import WorkType
from .models import Designation
from .models import Department
from .models import JobType

# Register your models here. "company"

admin.site.register(Company)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(JobType)
admin.site.register(WorkType)
admin.site.register(Holiday)
