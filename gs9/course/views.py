from django.shortcuts import render

# Create your views here.
def course(request):
    cname = 'django'
    duration = '4 months'
    seats = 10
    django_details = {'nm': cname, 'du':duration, 'st':seats}
    return render(request, 'course/course_home.html', django_details)



    # course = {'cname':'HARSHRAJ1'}
    # return render(request,'course/course_home.html',course)   #return render(request,'course/course_home.html',{'cname':'HARSHRAJ1'})