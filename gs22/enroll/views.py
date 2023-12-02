from django.shortcuts import render
from .models import Students

# Create your views here.
def home(request):
    return render(request,'enroll/home.html')

def student(request):
    student = Students.objects.all()
    return render(request,'enroll/student.html',{'stu':student})