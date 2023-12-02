from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('stu/',views.student,name='stu')
]
