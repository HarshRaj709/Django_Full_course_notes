from django.shortcuts import render
from .models import Student
from django.db.models import Avg,Sum,Min,Max,Count
# Create your views here.
def home(request):
    students = Student.objects.all()
    average = students.aggregate(Avg('marks'))
    max = students.aggregate(Max('marks'))
    min = students.aggregate(Min('marks'))
    sum = students.aggregate(Sum('marks'))
    count = students.aggregate(Count('marks'))
    print(average)
    print('return:',students)
    print()
    print('Sql Query:',students.query)
    return render(request,'school/home.html',{'students':students,'avg':average,'max':max,'min':min,'sum':sum,'count':count})