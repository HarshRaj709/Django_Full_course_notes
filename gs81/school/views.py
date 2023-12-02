from django.shortcuts import render
from django.db.models import Q
from .models import Student
from datetime import date,time
# Create your views here.
def home(request):
    # students = Student.objects.filter(Q(name='harsh Sahu') | Q(name='Akshay Dixit'))    #returns 2 records
    # students = Student.objects.filter(Q(name='harsh Sahu') & Q(roll=1))     #returns harsh sahu's data
    # students = Student.objects.filter(~Q(name='Akshay Dixit'))  # akshay ke alawa ke sare data de dega.
    # students = Student.objects.filter(Q(marks__gt=78) | Q(city='lucknow'))[:5]  #ye records upto 5 derha h.
    students = Student.objects.order_by('-name')[:5]    #descending order

    print('return:',students)
    print()
    print('Sql Query:',students.query)
    return render(request,'school/home.html',{'students':students})