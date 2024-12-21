from django.urls import path 
from .views import *

app_name='sheryiansapp'

urlpatterns=[
    path('',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('signin/',signin,name='signin'),
    path('requestCallBack/',requestCallBack,name='requestCallBack'),

]