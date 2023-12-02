from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.forms),
    path('success/',views.thankyou)
]
