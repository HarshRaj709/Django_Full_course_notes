from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.TemplateView.as_view(template_name = 'school/home.html'),name='home'),
    # path('index/',views.TemplateView.as_view(template_name = 'school/home.html'),name='home')
    # path('',views.Home.as_view(),name='home'),
    path('',views.Home.as_view(extra_context = {'course':'btech'}),name = 'home')
]
