from django.urls import path
from . import views

urlpatterns = [
    path('',views.StudentCreateView.as_view(template_name='school/forms.html'),name='form'),
    path('success/',views.success.as_view(),name='success'),
]
