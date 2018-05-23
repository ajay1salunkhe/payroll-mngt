from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^salary/$',views.salary,name='salary'),
    url(r'^salary/(?P<pk>\d+)/$',views.salary_emp,name='salary_emp'),
        url(r'^salary/details/(?P<pk>\d+)/(?P<month>\d+)/(?P<year>\d+)/$',views.salary_emp_details,name='salary_emp_details'),    
#    url(r'^salary/details/(?P<pk>\d+)/$',views.salary_emp_details,name='salary_emp_details'),    
    url(r'^salary/history/$',views.salary_history,name='salary_history'),
]
