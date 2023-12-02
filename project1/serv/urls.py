from django.urls import path
from . import views

urlpatterns = [
    path('serv/',views.services,name='serv')
]
