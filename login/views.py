from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import LoginForm
from user.models import Employee
from django.contrib.auth.models import User


# Create your views here.


def login_view(request):
    print("*"*10)
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("user : ",user)
        if form.is_valid():
            print("#"*10)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
        
    return render(request, 'login/login.html', {'form':form})

def logout_view(request):
    print("In logout view")
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request,'login/dashboard.html')


