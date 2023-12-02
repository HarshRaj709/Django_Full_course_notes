from django.shortcuts import render
from .models import Student
from datetime import date,time
# Create your views here.
def home(request):
    # students = Student.objects.all()

    # students = Student.objects.filter(name__exact = 'rahul')          #case sensitive
    # students = Student.objects.filter(name__iexact = 'Rahul')           # case insensitive

    # # students = Student.objects.filter(name__contains = 'y')           # retuns all names which have 'y' in it.
    # students = Student.objects.filter(city__contains = 'w')              # return all city names which contains 'w' in it.
    # students = Student.objects.filter(city__icontains = 'K')            # case insesitive

    # students = Student.objects.filter(id__in =[5,2,1] )
    # students = Student.objects.filter(id__in =[2] )         #list me hi dena hoga humko.
    # students = Student.objects.filter(marks__in =[98,100])

    # students = Student.objects.filter(marks__gte =80)

    # students = Student.objects.filter(name__startswith ='a')        #ye bhi case insensitive h

    # students = Student.objects.filter(name__endswith ='L')              #case insensitive

    # students = Student.objects.filter(passdate__range =('2023-09-01','2023-11-10'))      #ye range ke under ke sare return krta h
    
    # students = Student.objects.filter(admdatetime__date__gt=date(2023,11,4))       #return only those entries which created under the same date.
    # students = Student.objects.filter(admdatetime__year=2023)
    # students = Student.objects.filter(admdatetime__time__gt=time(6,00))

    students = Student.objects.filter(roll__isnull=False)       #false krne pr data de rha h, because isme data h.


    print('return:',students)
    print()
    print('Sql Query:',students.query)
    return render(request,'school/home.html',{'students':students})