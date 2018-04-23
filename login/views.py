from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import LoginForm, SignupUserForm, SignupCompanyForm, SignupEmployeeForm, SignupFormset
from user.models import Employee
from company.models import Company
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_view(request):
    return render(request,'login/home.html')

def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if form.is_valid():
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
        
    return render(request, 'login/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    return render(request,'login/dashboard.html')

def signup_view(request):
    if request.method=="POST":
        formCompany = SignupCompanyForm(request.POST)
        formUser = SignupUserForm(request.POST)
        formEmployee = SignupEmployeeForm(request.POST, request.FILES)
#        formSignup = SignupFormset() #request.POST, request.FILES)

        print("form1.is_valid() : ",formCompany.is_valid())
        print("form2.is_valid() : ",formUser.is_valid())
        print("form3.is_valid() : ",formEmployee.is_valid())
        print("formCompany.errors : ", formCompany.errors)
        print("formUser.errors : ", formUser.errors)
        print("formEmployee.errors : ", formEmployee.errors)
        if formCompany.is_valid() and formUser.is_valid() and formEmployee.is_valid():
            print("formCompany.cleaned_data : ", formCompany.cleaned_data)
            print("formUser.cleaned_data : ", formUser.cleaned_data)
            print("formEmployee.cleaned_data : ", formEmployee.cleaned_data)
            
            objCompany = formCompany.save()
            objUser = formUser.save(commit=False)
            objUser.set_password(objUser.password)
            objEmployee = formEmployee.save(commit=False)
            print(objEmployee, type(objEmployee))
            print("objCompany : ",objCompany.id)
#            objEmployee.company_id = objCompany
            objUser.save()
            objEmployee.company_id = objCompany
            objEmployee.user = objUser
            objEmployee.save()
            print("all valid")
    else:
        formCompany = SignupCompanyForm()
        formUser = SignupUserForm()
        formEmployee = SignupEmployeeForm()
#        formSignup = SignupFormset()
        
    return render(request,'login/signup.html',{'form1':formCompany, 'form2':formUser, 'form3':formEmployee}) #, 'form4':formSignup})

