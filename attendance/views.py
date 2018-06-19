from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from user.models import Employee, DesignationHistory
from attendance.models import Attendance
from company.models import WorkType, Designation, Holiday
from .forms import AttendanceForm, AttendanceHistoryForm, AttendanceHistoryByDateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
# Create your views here.

@login_required
def attendance(request):
    company_id = request.user.employee.company_id #obtaining current comp id
    emp = Employee.objects.filter(company_id=company_id)
    if request.method=="POST":
        formAttendance = AttendanceForm(request.POST, company_id=company_id)
        if formAttendance.is_valid():
            objAttendanceForm = formAttendance.save(commit=False)
            try:
                att_emp = Attendance.objects.filter(employee_id=objAttendanceForm.employee_id)
                
                if att_emp :
                    p_leave = Attendance.objects.filter(employee_id=objAttendanceForm.employee_id).latest('id').rem_privilege_leave
                    c_leave = Attendance.objects.filter(employee_id=objAttendanceForm.employee_id).latest('id').rem_casual_leave
                    objAttendanceForm.rem_privilege_leave = p_leave
                    objAttendanceForm.rem_casual_leave = c_leave

                    if Attendance.objects.filter(employee_id=objAttendanceForm.employee_id, date=objAttendanceForm.date).exists():
                        messages.warning(request, "Attendance already marked for this date")              
                    else:
                        if Holiday.objects.filter(company_id=request.user.employee.company_id,date=objAttendanceForm.date).exists():
                            messages.warning(request, "Attendance cant be marked on Holiday")
                            return redirect('attendance')
                        if objAttendanceForm.mark==0 and p_leave==0 and c_leave==0:
                            objAttendanceForm.lop = True
                            objAttendanceForm.save()
                            messages.success(request, "Attendance Submitted Successfully")                            
                        else:    
                            if objAttendanceForm.mark == 0 :
                                
                                if objAttendanceForm.leave_type == "PL" and p_leave>0 :
                                    objAttendanceForm.rem_privilege_leave -= 1
                                    objAttendanceForm.rem_casual_leave -= 0                            
                                elif objAttendanceForm.leave_type == "CL" and c_leave>0 :
                                    objAttendanceForm.rem_casual_leave -= 1
                                    objAttendanceForm.rem_privilege_leave -= 0
                                else:
                                    if c_leave!=0:
                                        objAttendanceForm.rem_casual_leave -= 1
                                        objAttendanceForm.rem_privilege_leave -= 0
                                    elif p_leave!=0:
                                        objAttendanceForm.rem_privilege_leave -= 1
                                        objAttendanceForm.rem_casual_leave -= 0                            
                            elif objAttendanceForm.mark == 1 :
                                objAttendanceForm.rem_privilege_leave -= 0
                                objAttendanceForm.rem_casual_leave -= 0

                            objAttendanceForm.save()
                            messages.success(request, "Attendance Submitted Successfully")
                            return redirect('attendance')
                    
                if not att_emp :
                    '''
                      this checks- current employee there is no attendance history 
                    no attendance history means no initialization of privilege and casual leaves
                    so here we are initializing leaves for first time and saves it in "Attendance" table
                    '''
                    print("objAttendanceForm.employee_id : ",objAttendanceForm.employee_id)
                    desig_id = DesignationHistory.objects.filter(employee_id=objAttendanceForm.employee_id).latest('id').designation_id                                    
                    p_leave = Designation.objects.filter(company_id=company_id,id=desig_id).latest('privilege_leave').privilege_leave
                    c_leave = Designation.objects.filter(company_id=company_id,id=desig_id).latest('casual_leave').casual_leave
                    objAttendanceForm.rem_privilege_leave = p_leave
                    objAttendanceForm.rem_casual_leave = c_leave                    
                    if objAttendanceForm.mark == 0 :
                        if objAttendanceForm.leave_type == "PL" :
                            objAttendanceForm.rem_privilege_leave -= 1
                            objAttendanceForm.rem_casual_leave -= 0                            
                        elif objAttendanceForm.leave_type == "CL" :
                            objAttendanceForm.rem_casual_leave -= 1
                            objAttendanceForm.rem_privilege_leave -= 0                            
                    elif objAttendanceForm.mark == 1 :
                        objAttendanceForm.rem_privilege_leave -= 0
                        objAttendanceForm.rem_casual_leave -= 0
                    objAttendanceForm.save()                 
            except:
                print("Something happened wrong  ")

    else:
       formAttendance = AttendanceForm(company_id=company_id)

    emps = Employee.objects.filter(company_id=request.user.employee.company_id)
    print("emps.count() : ",emps.count())
    present=[]
    absent=[]
    for emp in emps:
        if Attendance.objects.filter(date=datetime.datetime.today(),employee_id=emp.id,mark=1):
            present.append(emp)
        if Attendance.objects.filter(date=datetime.datetime.today(),employee_id=emp.id,mark=0):
            absent.append(emp)

    perc_present = round((len(present)/emps.count())*100,2)
    perc_absent = round((len(absent)/emps.count())*100,2)
    
    return render(request, 'attendance/attendance.html', {'form':formAttendance, 'present_emp':present, 'absent_emp':absent, 'perc_present':perc_present, 'perc_absent':perc_absent})

@login_required
def attendance_history(request):
    company_id = request.user.employee.company_id #obtaining current comp id
    emp = Employee.objects.filter(company_id=company_id)
    if request.method=="POST":
       formAttendance = AttendanceHistoryForm(request.POST, company_id=company_id)
       if formAttendance.is_valid():
           objFormAttendance = formAttendance.save(commit=False)
           fromdate = request.POST.get("fromdate")
           todate = request.POST.get("todate")
           selected_emp_id = objFormAttendance.employee.id
           selected_emp = Employee.objects.filter(id=selected_emp_id)
           print("selected_emp_id : ",selected_emp_id)
           print("selected_emp_name : ",selected_emp)           
           histories = Attendance.objects.filter(employee_id=selected_emp_id, date__gte=fromdate, date__lte=todate)
           for obj in histories:
               name = obj.employee
               print("name : ",name)
               break
           
           return render(request, 'attendance/attendance_history.html', {'employee':selected_emp,'history':histories, 'name':name})
    else:
       formAttendance = AttendanceHistoryForm(company_id=company_id)
       
    return render(request, 'attendance/attendance_history.html', {'form':formAttendance})

@login_required
def attendance_history_date(request):
    company_id = request.user.employee.company_id #obtaining current comp id
    emps = Employee.objects.filter(company_id=company_id)
    if request.method=="POST":
       formAttendance = AttendanceHistoryByDateForm(request.POST, company_id=company_id)
       if formAttendance.is_valid():
           s_date = datetime.datetime.strptime(request.POST.get('date'),"%Y-%m-%d").date()

       final = []
       for emp in emps:
           emp_m = list(Attendance.objects.filter(date=s_date,employee_id=emp.id).values('mark'))
           if len(emp_m)==0:
               emp_m = "(Not Marked)"
           elif len(emp_m)==1:
               emp_m = emp_m[0]['mark']
               if emp_m==1:
                   emp_m = "Present"
               if emp_m==0:
                   emp_m = "Absent"
           
           lt = list(Attendance.objects.filter(date=s_date,employee_id=emp.id).values('leave_type'))
           if len(lt)==0:
               lt = "---"
           elif len(lt)==1:
               lt = str(lt[0]['leave_type'])

           wt_id = list(Attendance.objects.filter(date=s_date,employee_id=emp.id).values('work_type_id'))
           print("wt_id",wt_id)
           if len(wt_id)==0:
               wt="---"
           elif len(wt_id)==1:
               if wt_id[0]['work_type_id'] == None:
                   wt="---"
               else:
                   wt = get_object_or_404(WorkType,id=wt_id[0]['work_type_id']).work_type
               
           dict1 = {
               "name":emp.name,
               "mark":emp_m,
               "lt":lt,
               "wt":wt
           }
           final.append(dict1)

 #          print("final : ",final)
           #emp_att.append(Attendance.objects.filter(date=date,employee_id=emp.id))
       return render(request, 'attendance/attendance_history_date1.html',{"final":final,"date":s_date})
    else:
       formAttendance = AttendanceHistoryByDateForm()
       
    return render(request, 'attendance/attendance_history_date.html', {'form':formAttendance})

