from django.shortcuts import render

# Create your views here.

def attendance(request):
    return render(request, 'attendance/attendance.html', {})

def attendance_history(request):
    print("In view attendance_history")
    return render(request, 'attendance/attendance_history1.html', {})

