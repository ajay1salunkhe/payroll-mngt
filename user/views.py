from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Employee
from django.views.generic import ListView
from .forms import employee_add_form
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

@login_required
def employee_display(request):
    queryset = Employee.objects.all()
    context = {

        "object_list": queryset,
    }

    return render(request, "base.html",context)

@login_required
def employee_add(request):

    if request.user.is_authenticated():
        #print("request.get_host() : ",request.get_host())
        if request.method=="POST":
            form=employee_add_form(request.POST or None, request.FILES)
            
            if form.is_valid():
                print("request.FILES : ",request.FILES)
                print("request.POST.get(profile_pic) : ",request.POST.get('profile_pic'))
                form.save()
                return redirect('employee_display')
        else:
            form=employee_add_form()
        return render(request, "employee_add.html",{'form':form}) 

    return redirect('employee_display')

def employee_update(request, pk):

    if request.user.is_authenticated():
        emp = get_object_or_404(Employee, pk=pk)

        if request.method=="POST":
            print("employee_update view and in POST")
            form=employee_add_form(request.POST,request.FILES,instance=emp)

            if form.is_valid():
                form.save()
                return redirect('employee_display')
        else:
            form=employee_add_form(instance=emp)
        
        return render(request, "employee_add.html",{'form':form})
        
    return redirect('employee_display')

    
