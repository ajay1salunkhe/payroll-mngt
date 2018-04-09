from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def attendance(request):
    return render(request, 'attendance/attendance.html', {})

@login_required
def attendance_history(request):
    print("In view attendance_history")
    return render(request, 'attendance/attendance_history.html', {})

