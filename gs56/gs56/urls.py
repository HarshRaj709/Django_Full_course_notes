"""
URL configuration for gs56 project.

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
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.UserSignup,name='signup'),
    path('login/',views.Userlogin,name='login'),
    path('profile/',views.UserProfile,name='profile'),
    path('logout/',views.Userlogout,name='logout'),
    path('password/',views.password1,name='password'),
    path('userdetail/<int:id>',views.userdetails,name='userdetail')
]
