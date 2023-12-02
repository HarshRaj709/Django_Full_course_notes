from django.urls import path
from . import views

urlpatterns = [
    path('stu/',views.stu,name='stu')
]