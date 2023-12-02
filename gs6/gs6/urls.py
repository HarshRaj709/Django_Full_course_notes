"""
URL configuration for gs6 project.

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
from course import views as cv
from fees import views as fv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cv.home),
    path('cor/',include([
        path('',cv.home),
        path('learn-py/', cv.learn_py),
        path('math/', cv.learn_m),
    ])),
    path('fees/', include([
        path('struct/',fv.fee_struct),
        path('ext/',fv.extra),
    ])),

]
