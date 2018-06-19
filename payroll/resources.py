from import_export import resources
from .models import SalaryHistory

class SalaryHistoryResource(resources.ModelResource):
        class Meta:
            model = SalaryHistory
