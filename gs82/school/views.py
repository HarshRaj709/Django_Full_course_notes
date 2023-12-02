from django.shortcuts import render
from .models import Student,Teacher

# Create your views here.
def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request,'school/home.html',{'students':students,'teachers':teachers})