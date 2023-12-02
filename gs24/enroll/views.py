from django.shortcuts import render
from .forms import userforms

# Create your views here.
def registration(request):
    #user = userforms(auto_id=False)
    user = userforms(auto_id='some_%s',label_suffix = ' ',initial={'names':'harsh','email':'harshsahu709@gmail.com'})
    return render(request,'enroll/registration.html',{'use':user})