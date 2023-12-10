from django.urls import path,include
from . import views

urlpatterns = [
    # path('accounts/',include('django.contrib.auth.urls')),      #iske through hi humare sare methods chalenge.. isko hum Project ke urls me bhi likh sakte h.
    path('profile/',views.profile,name='profile'),
    path('',views.home,name='home'),
]
