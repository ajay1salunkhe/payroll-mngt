from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Employee
from django.views.generic import ListView
#from .forms import PostForm


def employee_display(request):
    queryset = Employee.objects.all()
    context = {

        "object_list": queryset,
    }

    return render(request, "base.html",context)  

def employee_add(request):
    #temp = get_object_or_404()
    #print("hello view user")
    return render(request, "employee_add.html")  #,kwargs={ 'pk': str(self.id) }) #,{"temp":temp})  #index for test

