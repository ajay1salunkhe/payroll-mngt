from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.models import Employee, DesignationHistory, DepartmentHistory, EmployeeSalary
from .models import Salary, SalaryHistory
from attendance.models import Attendance
from company.models import Designation, Department, Holiday, WorkType
from .forms import select_emp_form, salary_emp_form, salary_history_form, salary_history_date_range
from user.forms import employee_salary_form
from django.core.exceptions import ObjectDoesNotExist
import datetime
import calendar
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
#from num2words import num2words

from weasyprint import HTML

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.core.mail import EmailMessage

#from .resources import SalaryHistoryResource

@login_required
def salary(request):
    company_id = request.user.employee.company_id #obtaining current comp id
    emp = Employee.objects.filter(company_id=company_id)
    if request.method=="POST":
        formSelectEmp = select_emp_form(request.POST)
        objformSelectEmp = formSelectEmp.save(commit=False)
        return redirect('salary_emp', pk=objformSelectEmp.employee.pk)
    else:
        formSelectEmp = select_emp_form(company_id=company_id)

    
        
    return render(request,'payroll/select_emp_salary.html',{'form':formSelectEmp})

@login_required
def salary_history(request):
    company_id = request.user.employee.company_id #obtaining current comp id
    emp = Employee.objects.filter(company_id=company_id)
    if request.method=="POST":
        formSelectEmp = select_emp_form(request.POST)
        objformSelectEmp = formSelectEmp.save(commit=False)
        fromdate = datetime.datetime.strptime(request.POST.get('fromdate'),"%Y-%m-%d").date()
        todate = datetime.datetime.strptime(request.POST.get('todate'),"%Y-%m-%d").date()
        print("fromdate : ",fromdate,"    todate : ",todate, "     type(fromdate) :",type(fromdate))
        return redirect('salary_history_show', pk=objformSelectEmp.employee.pk, fromdate=fromdate, todate=todate)
    else:
        formSelectEmp = select_emp_form(company_id=company_id)
        formDateRange = salary_history_date_range()
        
    return render(request, 'payroll/select_emp_for_history.html',{'form1':formSelectEmp,'form2':formDateRange})

@login_required
def salary_appraisal_history(request):
    company_id = request.user.employee.company_id #obtaining current comp id
    if request.method=="POST":
        formSelectEmp = select_emp_form(request.POST, company_id=company_id)
        if formSelectEmp.is_valid():
            objformSelectEmp = formSelectEmp.save(commit=False)
            empname = objformSelectEmp.employee.name
            salarys = EmployeeSalary.objects.filter(employee_id=objformSelectEmp.employee.pk)
            return render(request, 'payroll/appraisal_history.html',{'form1':formSelectEmp,'object_list':salarys, 'empname':empname})            
    else:
        formSelectEmp = select_emp_form(company_id=company_id)
        
    return render(request, 'payroll/appraisal_history.html',{'form1':formSelectEmp})

@login_required
def salary_update(request):
    company_id = request.user.employee.company_id #obtaining current comp id
    if request.method=="POST":
        formSelectEmp = select_emp_form(request.POST, company_id=company_id)
        formEmployeeSalary = employee_salary_form(request.POST)
        
        if formSelectEmp.is_valid() and formEmployeeSalary.is_valid():
            objformSelectEmp = formSelectEmp.save(commit=False)
            empname = objformSelectEmp.employee.name
            objformEmployeeSalary = formEmployeeSalary.save(commit=False)
            objformEmployeeSalary.employee_id = objformSelectEmp.employee.pk
            objformEmployeeSalary.updation_date = datetime.datetime.now().date()
            objformEmployeeSalary.save()
            salarys = EmployeeSalary.objects.filter(employee_id=objformSelectEmp.employee.pk)
            return render(request, 'payroll/appraisal_history.html',{'form1':formSelectEmp,'empname':empname, 'object_list':salarys})            
    else:
        formSelectEmp = select_emp_form(company_id=company_id)
        formEmployeeSalary = employee_salary_form()
        
    return render(request, 'payroll/appraisal_update.html',{'form1':formSelectEmp, 'form2':formEmployeeSalary})

@login_required
def salary_history_show(request,pk,fromdate,todate):
    empname = get_object_or_404(Employee, id=pk).name
    histories = SalaryHistory.objects.filter(employee_id=pk, date__gte=fromdate, date__lte=todate)
    return render(request, 'payroll/salary_history.html',{"empname":empname,"fromdate":fromdate,"todate":todate,"histories":histories,"empid":pk})

@login_required
def print_it(request,pk,month_year):
    empname = get_object_or_404(Employee, id=pk).name    
    emp_desig_id = DesignationHistory.objects.filter(employee_id=pk).latest('id').designation_id
    emp_depart_id = DepartmentHistory.objects.filter(employee_id=pk).latest('id').department_id
    emp_desig = get_object_or_404(Designation, id=emp_desig_id).designation
    emp_depart = get_object_or_404(Department, id=emp_depart_id).department

    print("month_year : ",month_year)
    start_date = datetime.datetime.strptime(month_year,"%m-%Y")
    end_date = datetime.datetime.strptime(
        str(start_date.year)+str(start_date.month)+str(calendar.monthrange(start_date.year,start_date.month)[1]),
        "%Y%m%d"
    )
    print("start_date : ",start_date,"     end_date : ",end_date)
    
    holidays = Holiday.objects.filter(company_id=request.user.employee.company_id,date__gte=start_date,date__lte=end_date).count()
    temp_date = start_date
    delta = datetime.timedelta(days=1)
    weekends = 0
    while temp_date <= end_date :
        if get_object_or_404(WorkType,company_id=request.user.employee.company_id).work_type == "SatSunHol":
            if temp_date.weekday()==5 or temp_date.weekday()==6 :
                weekends+=1
            temp_date+=delta
    try:
        p_leave = Attendance.objects.filter(employee_id=pk,date__gte=start_date,date__lte=end_date).latest('id').rem_privilege_leave
        c_leave = Attendance.objects.filter(employee_id=pk,date__gte=start_date,date__lte=end_date).latest('id').rem_casual_leave
    except ObjectDoesNotExist:
        p_leave = "?"
        c_leave = "?"
    
    history = get_object_or_404(SalaryHistory, employee_id=pk, month_year=month_year)
    
    html_string = render_to_string('payroll/html_for_pdf1.html',
                                   {
                                       "company":request.user.employee.company_id,
                                       "company_address":request.user.employee.company_id.address,                                           
                                       "empname":empname,
                                       "empdesig":emp_desig,
                                       "empdepart":emp_depart,
                                       "month_year":month_year,
                                       # "salary_date":datetime.datetime.now().date(),
                                       # "working_days":working_days,
                                       "weekends":weekends,
                                       "holidays":holidays,
                                       # "paid_days":paid_days,
                                       # "lop_days":lop_days,
                                       # "leaves":leaves,
                                       "p_leave":p_leave,
                                       "c_leave":c_leave,                                           
                                       # "basic":basic_amt,
                                       # "hra":hra_amt,
                                       # "convey_allow":conveyance_allow,
                                       # "special_allow":special_allow,
                                       # "proff_tax":proff_tax,
                                       # "income_tax":income_tax,
                                       # "lop":lop,
                                       # "gross_earning":gross_earning,
                                       # "gross_deduction":gross_deduction,
                                       # "net_salary":net_salary,
                                       "net_salary_in_words": "----",#num2words(history.net_salary),
                                       "obj":history,
                                       "pdf_gen_time":datetime.datetime.now(),
                                   }
    )    
    pdf_name = "s_"+empname.replace(" ","_")+"_"+str(datetime.datetime.now().date())
    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/salary.pdf');
    fs = FileSystemStorage('/tmp')
    with fs.open('salary.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename='+pdf_name+'.pdf'
        return response
    return response    
    
@login_required
def salary_emp(request, pk):
    try:
        empsal = Salary.objects.filter(employee_id=pk).latest('id')
    except ObjectDoesNotExist:
        emp_salary_id = EmployeeSalary.objects.filter(employee_id=pk, effective_from__lte=datetime.datetime.now().date()).latest('id').id
        emp_annual_sal = get_object_or_404(EmployeeSalary, id=emp_salary_id).salary
        gross_month = emp_annual_sal/12;
        empsal = Salary.objects.create(
            date=datetime.datetime.now().date(),
            employee_id=pk,
            gross_month_salary=gross_month,
        )
    
    empname = get_object_or_404(Employee, id=pk).name
    emp_salary_id = EmployeeSalary.objects.filter(employee_id=pk, effective_from__lte=datetime.datetime.now().date()).latest('id').id
    emp_annual_sal = get_object_or_404(EmployeeSalary, id=emp_salary_id).salary
    gross_month = emp_annual_sal/12;
    
    if request.method=="POST":
        formSalaryEmp = salary_emp_form(request.POST)
        if formSalaryEmp.is_valid():
            objformSalaryEmp = formSalaryEmp.save(commit=False)
            objformSalaryEmp.date = datetime.datetime.now()
            objformSalaryEmp.gross_month_salary = gross_month
            objformSalaryEmp.employee_id = pk
            emp_sal_previous = Salary.objects.filter(employee_id=pk).latest('id')
            objformSalaryEmp.save()

            date = datetime.datetime.strptime(request.POST.get('mdate'),"%Y-%m-%d").date()
            month = date.month
            year = date.year
            month_year = str(month)+"-"+str(year)
            
            if SalaryHistory.objects.filter(employee_id=pk,month_year=month_year).exists():
                messages.error(request,"Salary for this month and year is already exists")
            else:
                return redirect('salary_emp_details',pk=pk,month=month,year=year)
    else:
        formSalaryEmp = salary_emp_form(instance=empsal)
            
    return render(request, 'payroll/salary_details.html',{"form":formSalaryEmp,'empname':empname, 'gross_month':gross_month})    

def salary_emp_details(request,pk,month,year):
   try:
    empname = get_object_or_404(Employee, id=pk).name
    emp_desig_id = DesignationHistory.objects.filter(employee_id=pk).latest('id').designation_id
    emp_depart_id = DepartmentHistory.objects.filter(employee_id=pk).latest('id').department_id
    emp_desig = get_object_or_404(Designation, id=emp_desig_id).designation
    emp_depart = get_object_or_404(Department, id=emp_depart_id).department

    emp_salary_id = EmployeeSalary.objects.filter(employee_id=pk, effective_from__lte=datetime.datetime.now().date()).latest('id').id
    emp_annual_sal = get_object_or_404(EmployeeSalary, id=emp_salary_id).salary
    gross_month = emp_annual_sal/12;

    #default values will change later
    latest_sal_structure = Salary.objects.filter(employee_id=pk).latest('id')
    basic_perc = latest_sal_structure.basic_salary_perc
    hra_perc = latest_sal_structure.hra_perc
    income_tax_perc = latest_sal_structure.income_tax_perc
    conveyance_allow = float(latest_sal_structure.conveyance_allow)
    proff_tax = float(latest_sal_structure.prof_tax)
    
    basic_amt = (basic_perc/100)*float(gross_month) 
    hra_amt = (hra_perc/100)*basic_amt 
    income_tax = (income_tax_perc/100)*basic_amt 
    special_allow = float(gross_month) - (basic_amt+hra_amt+conveyance_allow+proff_tax+income_tax)
    month_year = str(month)+"-"+str(year)
    start_date = datetime.datetime.strptime(str(year)+str(month),"%Y%m")
    end_date = datetime.datetime.strptime(
        str(year)+str(month)+str(calendar.monthrange(start_date.year,start_date.month)[1]),
        "%Y%m%d"
    )

    
    working_days = Attendance.objects.filter(employee_id=pk,date__gte=start_date,date__lte=end_date,mark=1).count()
    leaves = Attendance.objects.filter(employee_id=pk,date__gte=start_date,date__lte=end_date,mark=0).count()
    paid_days = Attendance.objects.filter(employee_id=pk,date__gte=start_date,date__lte=end_date,lop="f").count()
    lop_days = Attendance.objects.filter(employee_id=pk,date__gte=start_date,date__lte=end_date,lop="t").count()
    holidays = Holiday.objects.filter(company_id=request.user.employee.company_id,date__gte=start_date,date__lte=end_date).count()
    temp_date = start_date
    delta = datetime.timedelta(days=1)
    weekends = 0
    list_of_incomplete_att = []
    while temp_date <= end_date :
        if not Attendance.objects.filter(employee_id=pk,date=temp_date):
            if temp_date.weekday()==5 or temp_date.weekday()==6 or Holiday.objects.filter(company_id=request.user.employee.company_id,date=temp_date).exists():
                pass
            else:
                list_of_incomplete_att.append(temp_date.day)
            
        if get_object_or_404(WorkType,company_id=request.user.employee.company_id).work_type == "SatSunHol":
            if temp_date.weekday()==5 or temp_date.weekday()==6 :
                weekends+=1
        temp_date+=delta

        
    total_days = calendar.monthrange(start_date.year,start_date.month)[1]
    actual_days = working_days+leaves+lop_days+holidays+weekends
    if actual_days < total_days :
        messages.warning(request, "Attendance for this month("+str(datetime.datetime.strptime(month,"%m").strftime("%B"))+"-"+str(year)+") is incomplete : "+str(total_days-actual_days)+" day's attendance missing -> "+str(list_of_incomplete_att))
        return redirect('salary_emp',pk=pk)
        
    p_leave = Attendance.objects.filter(employee_id=pk).latest('id').rem_privilege_leave
    c_leave = Attendance.objects.filter(employee_id=pk).latest('id').rem_casual_leave

    lop = (gross_month/calendar.monthrange(start_date.year,start_date.month)[1])*lop_days

    gross_earning = basic_amt+hra_amt+conveyance_allow+special_allow
    gross_deduction = proff_tax+income_tax+float(lop)
    net_salary = gross_earning-gross_deduction

    #rounding off for displying it on template
    gross_month=round(gross_month,2)
    basic_amt=round(basic_amt,2)
    hra_amt=round(hra_amt,2)
    conveyance_allow=round(conveyance_allow,2)    
    proff_tax=round(proff_tax,2)    
    income_tax=round(income_tax,2)
    special_allow=round(special_allow,2)
    lop=round(lop,2)
    gross_earning=round(gross_earning,2)
    gross_deduction=round(gross_deduction,2)
    net_salary=round(net_salary,2)
    
    if request.method=="POST":
        formSalaryHistory = salary_history_form(request.POST)

        if formSalaryHistory.is_valid():
            objformSalaryHistory = formSalaryHistory.save(commit=False)
            objformSalaryHistory.employee_id = pk
            objformSalaryHistory.date = datetime.datetime.now().date()
            objformSalaryHistory.month_year = month_year
            objformSalaryHistory.basic_perc = basic_perc
            objformSalaryHistory.basic = basic_amt
            objformSalaryHistory.hra_perc = hra_perc
            objformSalaryHistory.hra = hra_amt
            objformSalaryHistory.conveyance_allow = conveyance_allow
            objformSalaryHistory.special_allow = special_allow
            objformSalaryHistory.prof_tax = proff_tax
            objformSalaryHistory.income_tax_perc = income_tax_perc
            objformSalaryHistory.income_tax = income_tax
            objformSalaryHistory.loss_of_pay = lop
            objformSalaryHistory.gross_earning = gross_earning
            objformSalaryHistory.gross_deduction = gross_deduction
            objformSalaryHistory.working_days = working_days
            objformSalaryHistory.paid_days = paid_days
            objformSalaryHistory.net_salary = net_salary
            objformSalaryHistory.leaves = leaves
            objformSalaryHistory.lop_days = lop_days
            if SalaryHistory.objects.filter(employee_id=pk,month_year=month_year).exists():
                messages.error(request,"Error occured while saving")
                return redirect('salary_emp', pk=pk)
            else:
                objformSalaryHistory.save()
                
        html_string = render_to_string('payroll/html_for_pdf.html',
                                       {
                                           "company":request.user.employee.company_id,
                                           "company_address":request.user.employee.company_id.address,                                           
                                           "empname":empname,
                                           "empdesig":emp_desig,
                                           "empdepart":emp_depart,
                                           "month_year":month_year,
                                           "salary_date":datetime.datetime.now().date(),
                                           "working_days":working_days,
                                           "weekends":weekends,
                                           "holidays":holidays,
                                           "paid_days":paid_days,
                                           "lop_days":lop_days,
                                           "leaves":leaves,
                                           "p_leave":p_leave,
                                           "c_leave":c_leave,                                           
                                           "basic":basic_amt,
                                           "hra":hra_amt,
                                           "convey_allow":conveyance_allow,
                                           "special_allow":special_allow,
                                           "proff_tax":proff_tax,
                                           "income_tax":income_tax,
                                           "lop":lop,
                                           "gross_earning":gross_earning,
                                           "gross_deduction":gross_deduction,
                                           "net_salary":net_salary,
                                           "net_salary_in_words":"----",#num2words(net_salary),
                                           "pdf_gen_time":datetime.datetime.now(),
                                       }
        )
        
        pdf_name = "s_"+empname.replace(" ","_")+"_"+str(datetime.datetime.now().date())
        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/salary.pdf');
        fs = FileSystemStorage('/tmp')
        with fs.open('salary.pdf') as pdf:
            current_site = get_current_site(request)
            mail_subject = str(request.user.employee.company_id) + " : Salary Details"
            user_id = get_object_or_404(Employee, id=pk).user_id
            to_email =  get_object_or_404(User, id=user_id).email
#            to_email = "mail2ajaysalunkhe123@gmail.com"
            message = "Salary Details of Month : "+str(datetime.datetime.strptime(month,"%m").strftime("%B"))+" & Year : "+ str(year)
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.attach_file('/tmp/salary.pdf')
            email.send()
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename='+pdf_name+'.pdf'
            print("response : ",response)
            return response
                        
        return response
    else:
        pass
    
    return render(request, 'payroll/full_salary_details.html',
                  {
                      "empname":empname,
                      "empdesig":emp_desig,
                      "empdepart":emp_depart,
                      "basic":basic_amt,
                      "hra":hra_amt,
                      "convey_allow":conveyance_allow,
                      "special_allow":special_allow,
                      "proff_tax":proff_tax,
                      "income_tax":income_tax,
                      "lop":lop,
                      "month_year":month_year,
                      "salary_date":datetime.datetime.now().date(),
                      "working_days":working_days,
                      "weekends":weekends,
                      "holidays":holidays,
                      "paid_days":paid_days,
                      "lop_days":lop_days,
                      "leaves":leaves,
                      "p_leave":p_leave,
                      "c_leave":c_leave,
                      "gross_earning":gross_earning,
                      "gross_deduction":gross_deduction,
                      "net_salary":net_salary,
                      "net_salary_in_words":"----", #num2words(net_salary),
                  }
    )
   except e as Exception:
       messages.error(request,"Following error occured : ",e)

def export_to_csv(request, pk, fromdate, todate):
    res = SalaryHistoryResource()
    dataset = res.export()
    dataset.csv
