from django.forms import ModelForm
from .models import Employee, DesignationHistory, DepartmentHistory, JobTypeHistory, LeaveHistory, EmployeeSalary
from company.models import Designation, Department, JobType
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from django.forms.fields import DateField
from django.contrib import messages
from django.shortcuts import redirect
import datetime

class DateInput(forms.DateInput):
    input_type='date'

class user_add_form(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
#            'is_staff',
#           'is_superuser'
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Username',
                    'maxlength':'255'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter email here',
                    'maxlength':'255'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Password',
                    'maxlength':'255'
                }
            ),            
        }

        
class employee_add_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'name', 
            'address',
            'contact',
            'alt_contact',
#            'email',
            'gender',
            'dob',
            'pan_id',
            'aadhar_no',
            'profile_pic',
            'probation_period',
#            'company_id'
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter employee name here',
                    'maxlength':'255'
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter address here',
                    'maxlength':'255',
                    #'height':'10'
                }
            ),
            'contact': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter contact here',
                    'maxlength':'12'
                }
            ),
            'alt_contact': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter alt contact here',
                    'maxlength':'12'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter email here',
                    'maxlength':'255'
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                 #   'placeholder':'Enter email here',
                 #   'maxlength':'255'
                }
            ),
            'dob': DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter dob here',
                 #   'maxlength':'255'
                }
            ),
            'pan_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter pan id here',
                    'maxlength':'255'
                }
            ),
            'aadhar_no': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter aadhar no here',
                    'maxlength':'12'
                }
            ),
            'profile_pic': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Upload profile pic here',                    
                }
            ),
            'probation_period': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter probation period here',
                    'maxlength':'4'
                }
            ),
            'company_id': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

        }
        
        

class employee_designation_form(forms.ModelForm):
    class Meta:
        model = DesignationHistory
        fields = (
#            'employee',
            'designation',
#            'date',
        )
        widgets = {
            'designation': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),            
        }
        

    def __init__(self,temp,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['designation'].queryset = Designation.objects.filter(company_id=temp)

        # print("try latest id og des history : ", type(Designation.objects.filter(company_id=temp).latest('id').id) )
        # tid = DesignationHistory.objects.latest('id').designation_id
        # print("tid : ",tid)
#        self.initial['designation'] = Designation.objects.filter(company_id=temp).latest('id')
        

class employee_department_form(forms.ModelForm):
    class Meta:
        model = DepartmentHistory
        fields = (
            'department',
        )
        widgets = {
            'department': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),            
        }        

    def __init__(self,temp,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.filter(company_id=temp)      

class employee_job_type_form(forms.ModelForm):
    class Meta:
        model = JobTypeHistory
        fields = (
            'job_type',
        )
        widgets = {
            'job_type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),            
        }        

    def __init__(self,temp,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job_type'].queryset = JobType.objects.filter(company_id=temp)

class employee_salary_form(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = (
            'salary',
            'effective_from',
        )
        widgets = {
            'salary': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter salary here',
                    'maxlength':'7'
                }
            ),
            'effective_from': DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),            
        }                
