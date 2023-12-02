from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Harsh'
    request.session['lname'] = 'Sahu'
    request.session.set_expiry(60)
    return render(request,'student/setsession.html')

def getsession(request):
    name=request.session.get('name',default='guest')
    lname=request.session.get('lname',default='guest')
    return render(request,'student/getsession.html',{'name':name,'lname':lname})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'student/delsession.html')

def home(request):
    return render(request,'student/home.html')