from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("<h1>Home page</h1>")

def learn_py(request):
    return HttpResponse("love you python")

def learn_m(request):
    a = 20+20
    return HttpResponse(a)