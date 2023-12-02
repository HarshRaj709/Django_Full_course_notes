from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print('im View')
    return HttpResponse('this is home page')