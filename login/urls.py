from django.conf.urls import url
from . import views
import user.urls
import attendance.urls

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^employee/$',user.views.employee_display,name='employee_display'),
]
