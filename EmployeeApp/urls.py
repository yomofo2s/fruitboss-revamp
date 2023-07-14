#from django.conf.urls import url
from django.urls import path
from EmployeeApp import views

app_name = "EmployeeApp"

urlpatterns=[
    path("department/",views.departmentApi),
    path('department/([0-9]+)$',views.departmentApi)
]