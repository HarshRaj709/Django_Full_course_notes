from django.shortcuts import render
from .forms import studentforms
# Create your views here.

def stud(request):
    student = studentforms(initial={'name':'rohini','email':'harshraj@gmail.com'})
    return render(request,'enroll/forms.html',{'stds':student})


