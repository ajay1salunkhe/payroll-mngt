from django.conf.urls import url
from django.contrib import admin
#import user
from . import views
import login.views
import login.urls
import attendance.urls

urlpatterns = [
    url(r'^$', views.employee_display,name="employee_display"),
    url(r'^add/$', views.employee_add,name="employee_add"),
]
