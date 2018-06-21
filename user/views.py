from django.shortcuts import render ,get_object_or_404
1;4205;0cfrom django.http import HttpResponse
from django.shortcuts import redirect
from .models import Employee, DesignationHistory,DepartmentHistory, JobTypeHistory
from company.models import Designation, Department, JobType
from django.contrib.auth.models import User
from django.views.generic import ListView
from .forms import employee_add_form, user_add_form
from .forms import employee_designation_form, employee_department_form, employee_job_type_form, employee_salary_form
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db import transaction
import datetime
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages
#from .resources import EmployeeResource
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def employee_display(request):
    #    queryset = Employee.objects.all()
    queryset = Employee.objects.filter(company_id=request.user.employee.company_id.id)
    page = request.GET.get('page',1)

    paginator = Paginator(queryset,8)
    try:
        emps = paginator.page(page)
    except PageNotAnInteger:
        emps = paginator.page(1)
    except EmptyPage:
        emps = paginator.page(paginator.num_pages)
                
    # context = {
    #     "object_list": queryset,
    # }
    return render(request, "base.html",{"object_list":emps})    
#    return render(request, "base.html",context)

@login_required
@transaction.atomic
def employee_add(request):

    if request.user.is_authenticated():
        temp = request.user.employee.company_id #obtaining current comp id
        if request.method=="POST":
            formUser = user_add_form(request.POST)
            formEmployee = employee_add_form(request.POST or None, request.FILES)
            formEmployeeDesignation = employee_designation_form(temp,request.POST)
            formEmployeeDepartment = employee_department_form(temp,request.POST)
            formEmployeeJobType = employee_job_type_form(temp,request.POST)
            formEmployeeSalary = employee_salary_form(request.POST)
            if formUser.is_valid() and formEmployee.is_valid() and formEmployeeDesignation.is_valid() and formEmployeeDepartment.is_valid() and formEmployeeJobType.is_valid() and formEmployeeSalary.is_valid() :
                objUser = formUser.save(commit=False)
                plainpass = objUser.password
                objUser.set_password(objUser.password)
                objEmployee = formEmployee.save(commit=False)
                objUser.save()
                objEmployee.company_id =  request.user.employee.company_id
                objEmployee.user = objUser
                born = datetime.datetime.strptime(request.POST.get('dob'),"%Y-%m-%d").date()
                print("born : ",born)
                today = datetime.datetime.today()
                age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
                if age >=5 :
                    objEmployee.save()
                else:
                    messages.error(request,"Age should be greater than 5")
                emp = get_object_or_404(Employee, user_id=objEmployee.user)
                objEmployeeDesignation = formEmployeeDesignation.save(commit=False)           
                objEmployeeDesignation.employee = emp
                objEmployeeDesignation.date = datetime.datetime.now().date()
                objEmployeeDesignation.save()
                objEmployeeDepartment = formEmployeeDepartment.save(commit=False)
                objEmployeeDepartment.employee = emp
                objEmployeeDepartment.date = datetime.datetime.now().date()
                objEmployeeDepartment.save()
                objEmployeeJobType = formEmployeeJobType.save(commit=False)
                objEmployeeJobType.employee = emp
                objEmployeeJobType.date = datetime.datetime.now().date()
                objEmployeeJobType.save()         
                current_site = get_current_site(request)
                mail_subject = 'subject ----'
                to_email = objUser.email
                message = 'Your username is : '+objUser.username+' and password is : '+plainpass
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                objEmployeeSalary = formEmployeeSalary.save(commit=False)
                objEmployeeSalary.employee = emp
                objEmployeeSalary.updation_date = datetime.datetime.now().date()
                objEmployeeSalary.save()
                
                return redirect('employee_display')
        else:
            formUser = user_add_form()
            formEmployee = employee_add_form()
            formEmployeeDesignation = employee_designation_form(temp,initial={'designation':Designation.objects.last()})
            formEmployeeDepartment = employee_department_form(temp)
            formEmployeeJobType = employee_job_type_form(temp)
            formEmployeeSalary = employee_salary_form()
        return render(request, "employee_add.html",{'form1':formUser, 'form2':formEmployee, 'form3':formEmployeeDesignation,  'form4':formEmployeeDepartment,  'form5':formEmployeeJobType, 'form6':formEmployeeSalary })

    return redirect('employee_display')

@login_required
@transaction.atomic
def employee_update(request, pk):

    if request.user.is_authenticated():
        usr=get_object_or_404(User, pk=pk)
        emp = get_object_or_404(Employee, user_id=pk)
        temp = request.user.employee.company_id #obtaining current comp id
        try:
            latestDes = DesignationHistory.objects.filter(employee=emp).latest('id')
            dictDes = { #for passing initial to Designation field
                'date':latestDes.date,
                'employee':latestDes.employee,
                'designation': latestDes.designation,
            }            
        except:
            latestDes=None
            dictDes = { #for passing initial to Designation field
                'date':None,
                'employee':None,
                'designation': None,
            }
            
        try:
            latestDept = DepartmentHistory.objects.filter(employee=emp).latest('id')
            dictDept = { #for passing initial to Deptment field
                'date':latestDept.date,
                'employee':latestDept.employee,
                'department':latestDept.department,
            }
        except:
            latestDept=None
            dictDept = { #for passing initial to Deptment field
                'date':None,
                'employee':None,
                'department':None,
            }

        try:
            latestJobtype = JobTypeHistory.objects.filter(employee=emp).latest('id')
            dictJobtype = { #for passing initial to Jobtype field
                'date':latestJobtype.date,
                'employee':latestJobtype.employee,
                'job_type':latestJobtype.job_type,
            }
        except:
            latestJobtype=None
            dictJobtype = { #for passing initial to Jobtype field
                'date':None,
                'employee':None,
                'job_type':None,
            }            
             
        if request.method=="POST":
            formUser = user_add_form(request.POST,instance=usr)
            formEmployee = employee_add_form(request.POST or None,request.FILES,instance=emp)
            formEmployeeDesignation = employee_designation_form(temp,request.POST)
            formEmployeeDepartment = employee_department_form(temp,request.POST)
            formEmployeeJobType = employee_job_type_form(temp,request.POST)
            formEmployeeSalary = employee_salary_form(request.POST)            
            if formUser.is_valid() and formEmployee.is_valid():
                objUser = formUser.save(commit=False)
                objUser.set_password(objUser.password)                
                objUser.save()
                objEmployee = formEmployee.save(commit=False)
                objEmployee.company_id =  request.user.employee.company_id
                objEmployee.user = objUser                
                objEmployee.save()
                emp = get_object_or_404(Employee, user_id=objEmployee.user)
                objEmployeeDesignation = formEmployeeDesignation.save(commit=False)          
                objEmployeeDesignation.employee = emp
                objEmployeeDesignation.date = datetime.datetime.now().date()
                objEmployeeDesignation.save()
                objEmployeeDepartment = formEmployeeDepartment.save(commit=False)
                objEmployeeDepartment.employee = emp
                objEmployeeDepartment.date = datetime.datetime.now().date()
                objEmployeeDepartment.save()
                objEmployeeJobType = formEmployeeJobType.save(commit=False)
                objEmployeeJobType.employee = emp
                objEmployeeJobType.date = datetime.datetime.now().date()
                objEmployeeJobType.save()
                
                return redirect('employee_display')
        else:
            formUser=user_add_form(instance=usr)
            formEmployee=employee_add_form(instance=emp)
            formEmployeeDesignation = employee_designation_form(temp,initial=dictDes)
            formEmployeeDepartment = employee_department_form(temp,initial=dictDept)
            formEmployeeJobType = employee_job_type_form(temp,initial=dictJobtype)

            
    return render(request, "employee_add.html",{'form1':formUser, 'form2':formEmployee, 'form3':formEmployeeDesignation, 'form4':formEmployeeDepartment,  'form5':formEmployeeJobType})

def export_to_csv_employee(request):
    res = EmployeeResource()
    emps = Employee.objects.filter(company_id=request.user.employee.company_id)
    dataset = res.export(emps)
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    return response

def export_to_excel_employee(request):
    res = EmployeeResource()
    emps = Employee.objects.filter(company_id=request.user.employee.company_id)
    dataset = res.export(emps)
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="employees.xls"'
    return response

