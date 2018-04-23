from django import forms
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from user.models import Employee
from company.models import Company
from django.http import HttpResponse
from django.contrib.admin import widgets
from django.forms.fields import DateField
from django.forms import formset_factory

class DateInput(forms.DateInput):
    input_type='date'
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Username',
                    'required': 'required',
                    'autofocus': 'autofocus',
                    'style': 'margin-bottom: 7px;'
                }
            ),
            'password' : forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password',
                    'required': 'required',
                    'style': 'margin-bottom: 7px;'
                }
            ),
        }

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        

class SignupUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
#            'is_staff',
#            'is_superuser',
            'email'
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Username',
                    'required': 'required',
                    'autofocus': 'autofocus'
                  }
            ),
            'password' : forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password',
                    'required': 'required'
                }
            ),
            # 'email' : forms.EmailField(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Enter your valid email here'
            #     }
            # ),
        }

class SignupCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'namec','address','city','state','country','postal_code','fax','website'
        )

        widgets = {
            'namec': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter company name here',
                    'maxlength':'255'
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter company address here',
                    'maxlength':'255'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'city',
                    'maxlength':'255'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'state',
                    'maxlength':'255'
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'country',
                    'maxlength':'255'
                }
            ),
            'postal_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'postal code',
                    'maxlength':'255'
                }
            ),
            'fax': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'fax',
                    'maxlength':'255'
                }
            ),
            'website': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Enter Companys website here',
                    'maxlength':'255'
                }
            ),                        
        }

class SignupEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'name','address','contact','alt_contact','gender','dob','pan_id','aadhar_no','profile_pic','probation_period'
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
                    'placeholder':'Enter dob here'
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
        }
        
#class SignupForm():
SignupFormset = formset_factory(SignupUserForm, SignupCompanyForm, SignupEmployeeForm)
