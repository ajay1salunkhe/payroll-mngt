from django.conf.urls import url
from django.contrib import admin
#import user
from . import views
import login.views
import login.urls
import attendance.urls

urlpatterns = [
    url(r'^company/$', views.company_display,name="company_display"),
    url(r'^company/edit/$', views.company_edit,name="company_edit"),    
    # url(r'^company/add/$', views.company_add,name="company_add"),
    url(r'^holiday/add/$', views.holiday_add,name="holiday_add"),
    url(r'^holiday/delete/(?P<id>\d+)/$', views.holiday_delete,name="holiday_delete"),    
    url(r'^worktype/add/$', views.worktype_add,name="worktype_add"),
    url(r'^worktype/delete/(?P<id>\d+)/$', views.worktype_delete,name="worktype_delete"),    
    url(r'^designation/add/$', views.designation_add,name="designation_add"),
    url(r'^designation/delete/(?P<id>\d+)/$', views.designation_delete,name="designation_delete"),    
    url(r'^department/add/$', views.department_add,name="department_add"),
    url(r'^department/delete/(?P<id>\d+)/$', views.department_delete,name="department_delete"),    
    url(r'^job-type/add/$', views.job_type_add,name="job_type_add"),
    url(r'^job-type/delete/(?P<id>\d+)/$', views.job_type_delete,name="job_type_delete"),    
]
