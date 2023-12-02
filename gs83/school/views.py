from django.shortcuts import render
from .models import Examcenter,Student

# Create your views here.
def home(request):
    students = Student.objects.all()
    exam = Examcenter.objects.all()
    return render(request,'school/home.html',{'student':students,'exam':exam})