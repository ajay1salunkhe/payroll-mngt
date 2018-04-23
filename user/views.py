from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Employee
from django.contrib.auth.models import User
from django.views.generic import ListView
from .forms import employee_add_form, user_add_form
from .forms import employee_designation_form
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import datetime

@login_required
def employee_display(request):
#    queryset = Employee.objects.all()
    queryset = Employee.objects.filter(company_id=request.user.employee.company_id.id)
    context = {

        "object_list": queryset,
    }

    return render(request, "base.html",context)

@login_required
def employee_add(request):

    if request.user.is_authenticated():
        temp = request.user.employee.company_id #obtaining current comp id
        if request.method=="POST":
            formUser = user_add_form(request.POST)
            formEmployee = employee_add_form(request.POST or None, request.FILES)
            formEmployeeDesignation = employee_designation_form(temp,request.POST)            
            if formUser.is_valid() and formEmployee.is_valid() and formEmployeeDesignation.is_valid() :
                objUser = formUser.save(commit=False)
                objUser.set_password(objUser.password)
                objEmployee = formEmployee.save(commit=False)
                objUser.save()
                objEmployee.company_id =  request.user.employee.company_id
                objEmployee.user = objUser
                objEmployee.save()
                objEmployeeDesignation = formEmployeeDesignation.save(commit=False)
                emp = get_object_or_404(Employee, user_id=objEmployee.user)
                print("employee_add emp : ",emp)
                objEmployeeDesignation.employee = emp
                objEmployeeDesignation.date = datetime.datetime.now().date()
                objEmployeeDesignation.save()
                return redirect('employee_display')
        else:
            formUser = user_add_form()
            formEmployee = employee_add_form()
            formEmployeeDesignation = employee_designation_form(temp)
        return render(request, "employee_add.html",{'form1':formUser, 'form2':formEmployee, 'form3':formEmployeeDesignation}) 

    return redirect('employee_display')

@login_required
def employee_update(request, pk):

    if request.user.is_authenticated():
        usr=get_object_or_404(User, pk=pk)
        emp = get_object_or_404(Employee, user_id=pk)
        temp = request.user.employee.company_id #obtaining current comp id        
        if request.method=="POST":
            formUser = user_add_form(request.POST,instance=usr)
            formEmployee = employee_add_form(request.POST or None,request.FILES,instance=emp)
            # formEmployeeDesignation = employee_designation_form(temp,request.POST)         
            if formUser.is_valid() and formEmployee.is_valid():
                objUser = formUser.save(commit=False)
                objUser.set_password(objUser.password)                
                objUser.save()
                objEmployee = formEmployee.save(commit=False)
                objEmployee.company_id =  request.user.employee.company_id
                objEmployee.user = objUser                
                objEmployee.save()
                # objEmployeeDesignation = formEmployeeDesignation.save(commit=False)
                # objEmployeeDesignation.employee = objEmployee.user
                # objEmployeeDesignation.date = datetime.datetime.now().date()
                # objEmployeeDesignation.save()
                return redirect('employee_display')
        else:
            formUser=user_add_form(instance=usr)
            formEmployee=employee_add_form(instance=emp)
            # formEmployeeDesignation = employee_designation_form(temp)
            
    return render(request, "employee_add.html",{'form1':formUser,'form2':formEmployee}) #,  'form3':formEmployeeDesignation})
    
   
