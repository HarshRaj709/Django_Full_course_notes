from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('profile/',login_required(views.Profile.as_view()),name='profile'),
    path('about/',login_required(views.About.as_view()),name='about'),
    # path('about/',staff_member_required(views.About.as_view()),name='about'),
    path('contact/',views.Contact.as_view(),name='contact')
]
