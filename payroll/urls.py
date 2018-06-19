from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^salary/$',views.salary,name='salary'),
    url(r'^salary/(?P<pk>\d+)/$',views.salary_emp,name='salary_emp'),
        url(r'^salary/details/(?P<pk>\d+)/(?P<month>\d+)/(?P<year>\d+)/$',views.salary_emp_details,name='salary_emp_details'),    
#    url(r'^salary/details/(?P<pk>\d+)/$',views.salary_emp_details,name='salary_emp_details'),    
    url(r'^salary/history/$',views.salary_history,name='salary_history'),
    url(r'^salary/history/pdf/(?P<pk>\d+)/(?P<month_year>.+)/$',views.print_it,name='print_it'),
    url(r'^salary/history/(?P<pk>\d+)/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$',views.salary_history_show,name='salary_history_show'),
    url(r'^salary/csv/(?P<pk>\d+)/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$',views.export_to_csv,name='export_to_csv'),
    url(r'^salary/history/appraisal/$',views.salary_appraisal_history,name='salary_appraisal_history'),
    url(r'^salary/update/$',views.salary_update,name='salary_update'),    
]
