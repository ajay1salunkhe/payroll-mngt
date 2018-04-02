from django import forms
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserLogin

from django.http import HttpResponse
from user.models import Employee
tempUser=""
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        
        user=authenticate(username=username, password=password)
        #if user is not None:
            #login(request,user)
        print(username,password)
        print(user)

