from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('Profile_update/<int:pk>',views.UserInfoEdit.as_view(),name='Infoedit'),
    path('delete/<int:id>/',views.userdelete.as_view(),name='deleteinfo'),
]
