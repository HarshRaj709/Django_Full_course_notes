from django.shortcuts import render
from .forms import userforms

# Create your views here.
def registration(request):
    #user = userforms(auto_id=False)
    user = userforms(initial={'names':"hola"})
    return render(request,'enroll/registration.html',{'use':user})