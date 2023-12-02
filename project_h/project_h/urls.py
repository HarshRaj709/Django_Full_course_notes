from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Harsh's Project"
admin.site.site_title = "Harsh's Project Admin Pannel"
admin.site.index_title = "Welcome Master"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
