from django.shortcuts import render
from enroll.models import students

# Create your views here.
def home(request):
    return render(request,'enroll/home.html')

def student(request):
    data = students.objects.all()
    return render(request,'enroll/student.html',{'dat':data})