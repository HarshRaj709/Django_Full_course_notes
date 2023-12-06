from django.urls import path
from . import views

urlpatterns = [
    path('',views.ContactFormView.as_view(),name='home'),
    path('thankyou/',views.ThankyouTemp.as_view(),name='thanks'),
]
