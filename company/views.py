from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Company, Holiday, WorkType, Designation, Department, JobType
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from user.models import Employee
from .forms import company_add_form, holiday_add_form, worktype_add_form, designation_add_form, department_add_form, job_type_add_form
from django.contrib import messages

@login_required
def company_display(request):
    company = Company.objects.filter(pk=request.user.employee.company_id.id)
    worktype = WorkType.objects.filter(company_id=request.user.employee.company_id.id)
    designation = Designation.objects.filter(company_id=request.user.employee.company_id.id)
    department = Department.objects.filter(company_id=request.user.employee.company_id.id)
    jobtype = JobType.objects.filter(company_id=request.user.employee.company_id.id)
    return render(request, 'company/company.html',{
        'company': company,
        'worktype': worktype,
        'designation': designation,
        'department': department,
        'jobtype': jobtype
    })

@login_required
def company_edit(request):
    com = get_object_or_404(Company, pk=request.user.employee.company_id.id)
    # print("request.user.employee.company_id.id : ",request.user.employee.company_id.id)
    # print("com : ",com)
    if request.method=="POST":
        formCompany = company_add_form(request.POST, instance=com)
        if formCompany.is_valid():
            formCompany.save()
            return redirect('company_display')
    else:
        formCompany = company_add_form(instance=com)
    return render(request, 'company/company_edit.html',{'form':formCompany})

@login_required
def holiday_add(request):
    holidays = Holiday.objects.filter(company=request.user.employee.company_id.id)
    if request.method=="POST":
        form_holiday=holiday_add_form(request.POST)
        if form_holiday.is_valid():
            obj = form_holiday.save(commit=False)
            obj.company = request.user.employee.company_id
            obj.save()
            messages.add_message(request, messages.SUCCESS, "Holiday Added Successfully")
            return redirect('company:holiday_add')
    else:
        form_holiday=holiday_add_form()
    return render(request, "company/holiday_add.html", {'form':form_holiday,'h':holidays})

@login_required
def holiday_delete(request, id):
    Holiday.objects.filter(id=id).delete()
    return redirect('company:holiday_add')

@login_required
def worktype_add(request):
    worktypes = WorkType.objects.filter(company=request.user.employee.company_id.id)    
    if request.method=="POST":
        form_worktype=worktype_add_form(request.POST)
        print("request.POST : ",request.POST)
        print("form_worktype.is_valid() : ",form_worktype.is_valid())
        if form_worktype.is_valid():
            obj = form_worktype.save(commit=False)
            obj.company = request.user.employee.company_id
            obj.save()
            return redirect('company:worktype_add')
    else:
        form_worktype=worktype_add_form()
    return render(request, "company/worktype_add.html", {'form':form_worktype, 'wt':worktypes})

@login_required
def worktype_delete(request, id):
    WorkType.objects.filter(id=id).delete()
    return redirect('company:worktype_add')

@login_required
def designation_add(request):
    designations = Designation.objects.filter(company=request.user.employee.company_id.id)   
    if request.method=="POST":
        form_designation=designation_add_form(request.POST)
        if form_designation.is_valid():
            obj = form_designation.save(commit=False)
            obj.company = request.user.employee.company_id
            obj.save()            
            return redirect('company:designation_add')
    else:
        form_designation=designation_add_form()
    return render(request, "company/designation_add.html", {'form':form_designation,'designations':designations})

@login_required
def designation_delete(request, id):
    Designation.objects.filter(id=id).delete()
    return redirect('company:designation_add')

@login_required
def department_add(request):
    departments = Department.objects.filter(company=request.user.employee.company_id.id)
    if request.method=="POST":
        form_department=department_add_form(request.POST)
        if form_department.is_valid():
            obj = form_department.save(commit=False)
            obj.company = request.user.employee.company_id
            obj.save()                        
            return redirect('company:department_add')
    else:
        form_department=department_add_form()
    return render(request, "company/department_add.html", {'form':form_department,'departments':departments})

@login_required
def department_delete(request, id):
    Department.objects.filter(id=id).delete()
    return redirect('company:department_add')

@login_required
def job_type_add(request):
    jobtypes = JobType.objects.filter(company=request.user.employee.company_id.id)    
    if request.method=="POST":
        form_job_type=job_type_add_form(request.POST)
        if form_job_type.is_valid():
            obj = form_job_type.save(commit=False)
            obj.company = request.user.employee.company_id
            obj.save()                        
            return redirect('company:job_type_add')
    else:
        form_job_type=job_type_add_form()
    return render(request, "company/jobtype_add.html",{'form':form_job_type,'jobtypes':jobtypes})

@login_required
def job_type_delete(request, id):
    JobType.objects.filter(id=id).delete()
    return redirect('company:job_type_add')

# def company_add_success(request):
#     return render(request, "company/company_add_success.html")
