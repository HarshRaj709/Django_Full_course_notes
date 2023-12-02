from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.all()            #Ab humko normal order me dikhega.
    # students = Student.students.all()       #esse humko order_by('name') ke according output show kr rha h.
    return render(request,'school/home.html',{'student':students})