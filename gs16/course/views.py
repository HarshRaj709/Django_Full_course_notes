from django.shortcuts import render

# Create your views here.
def cour(request):
    return render(request,'course/course_info.html')