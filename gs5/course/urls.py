from course import views   #iski jagah pe yha pr hum "from . import views". iska matlab h ki currnet directory se views ko import krlo
from django.urls import path
urlpatterns = [
    path('',views.home),
    path('learn_py/',views.learn_py),
    path('learn_math/',views.learn_m),
]