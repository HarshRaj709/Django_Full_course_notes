from django.shortcuts import render,HttpResponse
from  datetime import datetime,timedelta

# Create your views here.
def setcookie(request):
    response = render(request,'student/setcookie.html')
    # response.set_cookie('name','harsh',expires=datetime.utcnow()+timedelta(days=2),)  #  max_age=5 ---->max_age = seconds after that it get deleted.
    response.set_cookie('name','Ashish',expires=datetime.utcnow()+timedelta(days=2),) #lastupdated value hi lega
    response.set_cookie('lname','harsh',expires=datetime.utcnow()+timedelta(days=2),) #append cookie
    return response

def getcookie(request):
    # name=request.COOKIES['name']
    name = request.COOKIES.get('name','guest')
    return render(request,'student/getcookie.html',{'name':name})

def deletecookie(request):
    response=render(request,'student/delcookie.html')
    response.delete_cookie('name')
    response.delete_cookie('lname')
    return response

def salted_cookie(request):
    response = render(request,'student/setsaltcookie.html')
    response.set_signed_cookie('username','Harsh709',salt='my_salt',max_age=60*60)
    # response = HttpResponse("Signed Cookie Created")
    #response.set_signed_cookie('username', 'john', salt='mysalt', max_age=3600)
    return response

def getsalted(request):
    name = request.get_signed_cookie('username',default='signed not matched',salt='my_salt')
    return render(request,'student/getsalted.html',{'name':name})

def delsalted(request):
    response=render(request,'student/deltedsalt.html')
    response.delete_cookie('username')
    return response

def home(request):
    return render(request,'student/home.html')

