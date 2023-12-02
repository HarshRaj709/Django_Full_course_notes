from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print('Im view')
    return HttpResponse('This is home page.')

def excp(request):
    print('exception occured')
    a=10/0
    return HttpResponse('This is Excp page.')

def user_info(request):
    print('Im user info view')
    context = {'name':'harsh'}
    return TemplateResponse(request,'blog/user.html',context)