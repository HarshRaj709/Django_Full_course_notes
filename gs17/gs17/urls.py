"""
URL configuration for gs17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('abhum yha pe kuch bhi likh sakte h/',views.about,name = 'about'),
    path('cor/',include('course.urls')),
    path('fees/',include('fees.urls'))  #ab isko humko url tag se attach krne ke liye hum yha pe  kuch nhi krenge balki iske fees.urls me jayenge wha pe name likhnge
]
