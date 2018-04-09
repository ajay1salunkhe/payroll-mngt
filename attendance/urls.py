from django.conf.urls import url
from . import views
import login.urls
import user.urls
import company.urls

urlpatterns = [
    url(r'^attendance/$', views.attendance, name='attendance'),
    url(r'^attendance/history/$', views.attendance_history, name='attendance_history'),
]
