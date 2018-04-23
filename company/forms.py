from django.forms import ModelForm
from django import forms
from .models import Company, Holiday, WorkType, Designation, Department, JobType
from django.shortcuts import redirect
from django.contrib.admin import widgets
from django.forms.fields import DateField
class DateInput(forms.DateInput):
    input_type='date'
    
class company_add_form(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'namec',
            'address',
            'city',
            'state',
            'country',
            'postal_code',
            'fax',
            'website'
        )
        widgets = {
            'namec': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'postal_code': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'fax': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'website': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),            
        }
        

class holiday_add_form(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = (
#            'company',
            'date',
            'name'
        )
        widgets = {
            'date': DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter dob here'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter Holiday here'
                }
            ),            
        }


class worktype_add_form(forms.ModelForm):
    class Meta:
        model = WorkType
        fields = (
#            'company',
            'work_type',
        )
        widgets = {
            'work_type': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter Work Type here'
                }
            ),            
        }

class designation_add_form(forms.ModelForm):
    class Meta:
        model = Designation
        fields = (
#            'company',
            'designation',
            'privilege_leave',
            'casual_leave',
            'salary'
        )
        widgets = {
            'designation': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter Work Type here'
                }
            ),
            'privilege_leave': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'casual_leave': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'salary': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),           
        }
        
        
class department_add_form(forms.ModelForm):
    class Meta:
        model = Department
        fields = (
#            'company',
            'department',
        )
        widgets = {
            'department': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter Department here'
                }
            ),            
        }

class job_type_add_form(forms.ModelForm):
    class Meta:
        model = JobType
        fields = (
#            'company',
            'job_type',
        )        
        widgets = {
            'job_type': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter Job Type here'
                }
            ),            
        }
