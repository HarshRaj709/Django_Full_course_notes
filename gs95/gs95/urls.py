from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.TemplateView.as_view(template_name='school/home.html'),name='blankhome'),
    # path('home/',views.RedirectView.as_view(url='/'),name='home')
    path('home/',views.Redirects.as_view(),name='home'),     #through child class
    path('index/',views.RedirectView.as_view(pattern_name = 'home'),name='index'),
    path('home/<int:pk>/',views.redirect.as_view(),name = 'home_through_redirect'),     #main me ja rha h aur humara pk show nhi ho rha h template me.
    # path('index/<int:pk>/',views.TemplateView.as_view(template_name='school/index.html'),name='template_data')  #isme humko ab data mil rha h pk ka
    # path('<int:pk>/',views.TemplateView.as_view(template_name='school/home.html'),name='template_data')  #isme humko ab data mil rha h pk ka
    path('<slug:post>/',views.TemplateView.as_view(template_name='school/home.html'),name='template_data')  #passing slug value
    



]

