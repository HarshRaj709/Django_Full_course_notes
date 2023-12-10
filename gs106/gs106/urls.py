from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('registration.urls')),
    path('accounts/',include('registration.urls')),         #yha pe humko accounts/ ke bad app ke urls.py me pahuchana h.
    path('accounts/',include('django.contrib.auth.urls')),
]
