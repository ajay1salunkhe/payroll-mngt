from django.forms import ModelForm
from django import forms
from user.models import Employee
from .models import Salary, SalaryHistory
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from django.forms.fields import DateField
from django.contrib import messages
from django.shortcuts import redirect

class DateInput(forms.DateInput):
    input_type='date'

class select_emp_form(forms.ModelForm):
    class Meta:
        model = Salary
        fields = (
            'employee',
        )
        widgets = {
            'employee': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('company_id', False)
        super().__init__(*args, **kwargs)
        if company_id:
            self.fields['employee'].queryset = Employee.objects.filter(company_id=company_id)

class salary_emp_form(forms.ModelForm):
    mdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control',}))
    class Meta:
        model = Salary
        fields = (
#            'date',
            'mdate',
            'gross_month_salary',
            'basic_salary_perc',
            'hra_perc',
            'conveyance_allow',
            'prof_tax',
            'income_tax_perc',
        )
        widgets = {
            'gross_month_salary': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'basic_salary_perc': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'hra_perc': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'conveyance_allow': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'prof_tax': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'income_tax_perc': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),            
        }

        
class salary_history_form(forms.ModelForm):
    class Meta:
        model = SalaryHistory
        fields = ()


class salary_history_date_range(forms.Form):
        fromdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control', 'required': True}))
        todate = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control', 'required': True}))
