from django.conf.urls import url
from . import views
import user.urls
import attendance.urls
import company.urls

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),    
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^employee/$',user.views.employee_display,name='employee_display'),
    url(r'^company/$',company.views.company_display,name='company_display'),
    url(r'^attendance/$',attendance.views.attendance,name='attendance'),
]
