from django.urls import path
from . import views

urlpatterns = [
    path('<int:my_id>/',views.show_details,name='details'),   #show_details() got an unexpected keyword argument 'my_id', when we not added my_id in our views.py function
    path('<int:my_id>/<int:my_subid>/',views.show_subdetails,name='subdetails'),
]
