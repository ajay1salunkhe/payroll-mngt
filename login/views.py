from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import LoginForm, SignupUserForm, SignupCompanyForm, SignupEmployeeForm, SignupFormset
from user.models import Employee, DesignationHistory
from company.models import Company
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from payroll.models import SalaryHistory
from company.models import Designation
import datetime
import calendar
from django.db.models import Sum
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
    #try for chart :)
    now = datetime.datetime.now().date()
    l=[]
    l.append(0)
    for i in range(1,13):
        start_date = datetime.datetime.strptime(str(now.year)+str(i),"%Y%m")
        end_date = datetime.datetime.strptime(
            str(start_date.year)+str(i)+str(calendar.monthrange(start_date.year,start_date.month)[1]),
            "%Y%m%d"
        )
        total = SalaryHistory.objects.filter(date__gte=start_date,date__lte=end_date).aggregate(Sum('net_salary'))
        if total['net_salary__sum']==None:
            l.append(0)
        else:
            l.append(int(total['net_salary__sum']))

    #try for pie chart :)
    d = list(Designation.objects.filter(company_id=request.user.employee.company_id).values('designation'))
    l2=[]
    for i in d:
        l2.append(i['designation'])

    empdictlist = list(Employee.objects.filter(company_id=request.user.employee.company_id).values('id'))
    employees=[]
    for i in empdictlist:
        employees.append(i['id'])
    
    l3=[]
    for i in l2:
        temp=0
        for j in employees:
            latest_des_id = DesignationHistory.objects.filter(employee_id=j).latest('id').designation_id
            des = list(Designation.objects.filter(id=latest_des_id).values('designation'))
            des = des[0]['designation']
            if i == des:
                temp+=1
        l3.append(temp)
                
    print("l3 : ",l3)

    #todays birthday try :)
    birthday_emp = Employee.objects.filter(company_id=request.user.employee.company_id,dob=now)

    print("birthday_emp : ",birthday_emp)

    #male female ratio
    males = Employee.objects.filter(company_id=request.user.employee.company_id,gender="M").count()
    females = Employee.objects.filter(company_id=request.user.employee.company_id,gender="F").count()
    
    return render(request,'login/dashboard.html',
                  {
                      "a1":l[1],
                      "a2":l[2],
                      "a3":l[3],
                      "a4":l[4],
                      "a5":l[5],
                      "a6":l[6],
                      "a7":l[7],
                      "a8":l[8],
                      "a9":l[9],
                      "a10":l[10],
                      "a11":l[11],
                      "a12":l[12],
                      "l2":l2,
                      "l3":l3,
                      "birthday_emp":birthday_emp,
                      "males":males,
                      "females":females,
                  }
    )

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
            '''
            email = EmailMessage('Subject', 'Body', to=[''])
            email.send()
            #res = send_mail('subject','message','mail2ajaysalunkhe123@gmail.com',['mail2ajaysalunkhe123@gmail.com'], fail_silently=False,)
            #print("res : ",res) '''
            print("all valid")
    else:
        formCompany = SignupCompanyForm()
        formUser = SignupUserForm()
        formEmployee = SignupEmployeeForm()
#        formSignup = SignupFormset()
        
    return render(request,'login/signup.html',{'form1':formCompany, 'form2':formUser, 'form3':formEmployee}) #, 'form4':formSignup})

