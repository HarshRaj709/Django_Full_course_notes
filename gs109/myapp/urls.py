from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),     #now it will work perfectlly
    # path('dashboard/',views.dashboard,name='dash'),
    path('dashboard/',TemplateView.as_view(template_name='myapp/dash.html')),       #esse bhi templateview ko render kr sakte h.
    # path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('logout/',views.CustomLogoutView.as_view(),name='logout'),
    # path('change_password/',auth_views.PasswordChangeView.as_view(template_name='myapp/passchange.html'),name='passchange'),
    path('change_password/',views.CustomizePassword.as_view(),name='custopass'),
]
