from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='detailpost'),
]
