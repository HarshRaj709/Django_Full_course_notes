from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    # students = Student.objects.all() 
    students = Student.students.get_roll(9013,9020)           
    return render(request,'school/home.html',{'student':students})