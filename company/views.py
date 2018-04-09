from django.shortcuts import render
from django.http import HttpResponse
from .models import Company
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

@login_required
def company_display(request):
    queryset = Company.objects.all()
    context = { "object_list": queryset,}
    return render(request, 'company/company.html',context)

@login_required
def company_add(request):
    return render(request, 'company/company_add.html',{})
