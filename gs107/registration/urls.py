from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('about/',views.about,name='about'),
    path('normal_about/',views.normal_about,name='normal')
]
