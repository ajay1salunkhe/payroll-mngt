from django.forms import ModelForm
from .models import Employee
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from django.forms.fields import DateField
from django.contrib import messages
from django.shortcuts import redirect

class DateInput(forms.DateInput):
    input_type='date'
    
class employee_add_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'name', 
            'address',
            'contact',
            'alt_contact',
            'email',
            'gender',
            'dob',
            'pan_id',
            'aadhar_no',
            'profile_pic',
            'probation_period',
            'company_id'
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

        try:
            employees=Employee.objects.all()
            for n in employees:
                s=str(n)
                if name==s:
                    print("duplicate entry : ",s)
                    return redirect('employee_add')
        except:
            print("name duplicate success")
    

