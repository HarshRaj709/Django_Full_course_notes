from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cl/',views.Hom2.as_view(name='harsh'),name='class'),           #ab name me harsh ayega yha ke argument ki value jada h
    path('child/',views.Myviewchild.as_view(),name='child')     #url of child class
]
