from django import forms
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.admin import widgets

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
        
        #user=authenticate(username=username, password=password)
        #if user is not None:
            #login(request,user)
        print(username,password)
        #print(user)

