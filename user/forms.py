from django.forms import ModelForm
from .models import Employee, DesignationHistory, DepartmentHistory, JobTypeHistory, LeaveHistory
from company.models import Designation
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from django.forms.fields import DateField
from django.contrib import messages
from django.shortcuts import redirect

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
        
        
    def clean(self):
        cleaned_data=self.cleaned_data
        name=cleaned_data.get('name')
        email=cleaned_data.get('email')

        if Employee.objects.filter(name=name).exists():
            print("name already exists")

class employee_designation_form(forms.ModelForm):
    class Meta:
        model = DesignationHistory
        fields = (
#            'employee',
            'designation',
#            'date',
        )

    def __init__(self,temp,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['designation'].queryset = Designation.objects.filter(company_id=temp)
