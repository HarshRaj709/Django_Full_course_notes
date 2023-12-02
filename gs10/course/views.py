from django.shortcuts import render
from datetime import datetime

# Create your views here.
def course(request):
    dt = datetime.now()
    my_datetime = datetime(2023, 9, 25, 15, 30, 0)
    #dict = {'names':['harsh','rahul','abhiraj','harshraj']}
#     students = {'name':'harsh'} #iska ab use nhi kiya h 
#     name = 'harsh'
#     class1 = 'btech'
#     dict = {'nm':name,
#             'cls':class1}
    #return render(request,'course/course_home.html',dict)
    dict = {'my_datetime':my_datetime,'dt':dt,'nm':True,'st':'harsh','names':['harish','harshraj','harsh','rahul']}
    #return render(request,'course/course_home.html',{'d':dt})
    return render(request,'course/course_home.html',{'dicts':dict})  #yha pe humne phle only dict ko pass kiya tha wo bhi theek tha but usse hum log dictionary ki values ko access nhi kr sakte the isiliye ye kr diya
#     return render(request,'course/course_home.html',dict)
#     return render(request,'course/course_home.html',{'nm': False})
      