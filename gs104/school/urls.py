from django.urls import path
from . import views

urlpatterns = [
    path('',views.StudentCreate.as_view(),name='home'),
    path('update/<int:pk>',views.StudentUpdate.as_view(),name='update'),        #Generic detail view StudentUpdate must be called with either an object pk or a slug in the URLconf.
    path('success/',views.Success.as_view(),name='success'),
    path('all/',views.Allstudents.as_view(),name='all'),
    path('updated/',views.updated.as_view(template_name='school/updated.html'))
]