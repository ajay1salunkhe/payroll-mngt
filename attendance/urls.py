from django.conf.urls import url
from . import views
import login.urls
import user.urls

urlpatterns = [
    url(r'', views.attendance, name='attendance'),
    url(r'^history/$', views.attendance_history, name='attendance_history'),
]
