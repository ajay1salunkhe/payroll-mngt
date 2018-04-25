from django.forms import ModelForm
from django import forms
from .models import Attendance
from user.models import Employee
from company.models import WorkType
from django.forms.fields import DateField
import datetime
class DateInput(forms.DateInput):
    input_type='date'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = (
            'employee',
            'work_type',
            'date',
            'mark',
#            'rem_privilege_leave',
#            'rem_casual_leave',
            'leave_type'
        )
        widgets = {
            'employee': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'date': DateInput(
                attrs={
                    'class': 'form-control',
                    'value': datetime.datetime.now().date()
                }
            ),
            'work_type': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'mark': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'leave_type': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),            
        }

    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('company_id', False)
        super().__init__(*args, **kwargs)
        if company_id:
            self.fields['employee'].queryset = Employee.objects.filter(company_id=company_id)
            self.fields['work_type'].queryset = WorkType.objects.filter(company_id=company_id)
