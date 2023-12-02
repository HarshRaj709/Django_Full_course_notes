from django.shortcuts import render

# Create your views here.
def course(request):
    course = 'B-tech'
    branch = 'cse'
    fees = 78000
    dict = {'course':course,'branch':branch,'fees':fees}
    return render(request,'course/course_home.html',{'doc':dict})