from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    # students = Student.objects.all()            #humko yha pe 'objects' ki jagah manlo 'students' se access krna h to uske liye hi ye sara prishram h.
    students = Student.students.all()       #ab ye humara kaam krega
    return render(request,'school/home.html',{'student':students})