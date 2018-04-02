from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import LoginForm
from user.models import Employee
from django.contrib.auth.models import User


# Create your views here.


def login(request):
    print("*"*10)
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            print("#"*10)
            if user is not None:
                return redirect('dashboard')
        
    return render(request, 'login/login.html', {})


def dashboard(request):
    return render(request,'login/dashboard.html')


