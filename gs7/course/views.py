from django.shortcuts import render

# Create your views here.
def course(request):
    return render(request,'course_home.html')