from django.shortcuts import render,HttpResponse
from . import signals

# Create your views here.
def home(request):
    signals.notification.send(sender=request,user=['geeky','shows'])
    return HttpResponse('THis is home page.')