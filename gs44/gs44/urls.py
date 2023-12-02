"""
URL configuration for gs44 project.

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
    path('student/<int:my_id>/',views.show_details,name='details'),   #show_details() got an unexpected keyword argument 'my_id', when we not added my_id in our views.py function
    path('',views.home,name='ghar'),
    path('student/<int:my_id>/<int:my_subid>/',views.show_subdetails,name='subdetails'),
]
