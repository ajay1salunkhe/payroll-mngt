from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

#import user
from . import views
import login.views
import login.urls
import attendance.urls

urlpatterns = [
    url(r'^employee/$', views.employee_display,name="employee_display"),
    url(r'^employee/add/$', views.employee_add,name="employee_add"),
    url(r'^employee/(?P<pk>\d+)/update/$',views.employee_update,name="employee_update"),
#    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
