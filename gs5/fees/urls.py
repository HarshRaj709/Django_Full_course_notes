from fees import views
from django.urls import path


urlpatterns = [
    path('fees/',views.fee_struct),
    path('extra/',views.extra),
]