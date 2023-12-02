from django.shortcuts import render

# Create your views here.
def course(request):
    name = 'harsh sahu'
    dict = {'nm':name}
    return render(request,'course/course_home.html',dict)