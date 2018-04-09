from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^salary/$',views.salary,name='salary'),
    url(r'^salary/history/$',views.salary_history,name='salary_history'),
]
