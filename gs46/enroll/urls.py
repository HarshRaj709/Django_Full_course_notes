from django.urls import path,register_converter
from . import views,converters

register_converter(converters.FourDigitYearConverter,'yyyy')

urlpatterns = [
    path('session/<yyyy:year>/',views.show_details,name='details'),
]
