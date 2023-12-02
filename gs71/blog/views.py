from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def home(request):
    a=10/0
    return HttpResponse('hello')