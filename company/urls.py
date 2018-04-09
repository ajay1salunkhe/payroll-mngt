from django.conf.urls import url
from django.contrib import admin
#import user
from . import views
import login.views
import login.urls
import attendance.urls

urlpatterns = [
    url(r'^company/$', views.company_display,name="company_display"),
    url(r'^company/add/$', views.company_add,name="company_add"),
]
