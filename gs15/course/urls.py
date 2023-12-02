from django.urls import path
from . import views

urlpatterns = [
    path('cour/',views.course)
]