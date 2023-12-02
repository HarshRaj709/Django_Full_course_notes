from django.urls import path
from . import views

urlpatterns = [
    path('stu/',views.student,name = 'stu'),
    path('form/',views.showformdata,name = 'form'),
]