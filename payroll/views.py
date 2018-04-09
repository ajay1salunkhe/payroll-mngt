from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def salary(request):
    return render(request,'payroll/salary.html')

@login_required
def salary_history(request):
    return render(request, 'payroll/salary_history.html')
