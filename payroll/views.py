from django.shortcuts import render
from .models import Employee
from django.utils import timezone

# Create your views here.

def post_list(request):
    employees = Employee.objects.filter(joining_date__lte=timezone.now()).order_by('joining_date')
    return render(request,'payroll/post_list.html',{'employees':employees})
