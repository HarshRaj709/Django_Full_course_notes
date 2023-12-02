from django.shortcuts import render
from enroll.models import hostel

# Create your views here.
def home(request):
    return render(request,'enroll/home.html')


def stu(request):
    host = hostel.objects.get(pk=2)
    return render(request,'enroll/students.html',{'hos':host})