from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from user.models import Employee, DesignationHistory
from attendance.models import Attendance
from company.models import WorkType, Designation
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def attendance(request):
    company_id = request.user.employee.company_id #obtaining current comp id
    emp = Employee.objects.filter(company_id=company_id)
    if request.method=="POST":
        formAttendance = AttendanceForm(request.POST)
        if formAttendance.is_valid():
            objAttendanceForm = formAttendance.save(commit=False)
            try:
                att_emp = Attendance.objects.filter(employee_id=objAttendanceForm.employee_id)

                
                if att_emp :
                    p_leave = Attendance.objects.filter(employee_id=objAttendanceForm.employee_id).latest('id').rem_privilege_leave
                    c_leave = Attendance.objects.filter(employee_id=objAttendanceForm.employee_id).latest('id').rem_casual_leave
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
                    
                if not att_emp :
                    '''
                      this checks- current employee there is no attendance history 
                    no attendance history means no initialization of privilege and casual leaves
                    so here we are initializing leaves for first time and saves it in "Attendance" table
                    '''
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
                    
                    print("*********************************************************")                                        
            except:
                print("Something happened wrong")

    else:
       formAttendance = AttendanceForm(company_id=company_id)

    return render(request, 'attendance/attendance.html', {'form':formAttendance})

@login_required
def attendance_history(request):
    return render(request, 'attendance/attendance_history.html', {})

