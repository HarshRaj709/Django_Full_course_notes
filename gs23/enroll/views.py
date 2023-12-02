from django.shortcuts import render
from .forms import studentRegistration

# Create your views here.
def home(request):
    return render(request,'enroll/home.html')

def student(request):
    return render(request,'enroll/student.html')

def showformdata(request):
    fm = studentRegistration
    return render(request,'enroll/userregistration.html',{'form':fm})