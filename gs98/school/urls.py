from django.urls import path
from . import views

urlpatterns = [
    path('',views.Studentlist.as_view(),name='home'),
    path('details/<int:id>',views.StudentDetails.as_view(),name='details'),        #Generic detail view StudentDetails must be called with either an object pk or a slug in the URLconf.
    
    # path('details/<int:pk>',views.StudentDetails.as_view(),name='details'),
    #Generic detail view StudentDetails must be called with either an object pk or a slug in the URLconf.
]
