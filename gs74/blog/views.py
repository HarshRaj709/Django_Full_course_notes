from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print('Im view')
    return HttpResponse('This is home page.')