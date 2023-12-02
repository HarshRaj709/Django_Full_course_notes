from django.shortcuts import render
from django.db.models import Count
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.
def home(request):
    # students = Student.objects.all()
    # students = Student.objects.all()[5:]

    # students = Student.objects.filter(Name = 'Harsh Sahu')
    # students = Student.objects.filter(Marks = 98)               #isme greater than and lessthan work nhi kr rha h.
    # students = Student.objects.filter(Marks__lt=90)         #less than ke liye lt
    # students = Student.objects.filter(Marks__gt=90)             # greater than ke liye marks__gt
    # students = Student.objects.filter(Marks__lte =90)               # less than or equal to
    # students = Student.objects.filter(Marks__gte =90)               # greater than or equal to.
    # students = Student.objects.filter(Name='Harsh Sahu').filter(city='lucknow')

    # students = Student.objects.order_by('Name')          # Capital alpahbet phle ayega small wale baad me,ex-A phle a bad me.
    # students = Student.objects.order_by('Name').reverse()       #isse name ka order reverse ho kr ayega
    # students = Student.objects.order_by('Name').reverse()[:5]       #only last ke 5 reverse ho kr ayenge.
    # students = Student.objects.order_by('?')        # normally ascending, -id : descending , ? : Random
    # students = Student.objects.order_by('id')        # normally ascending, -id : descending , ? : Random
    
    # students = Student.objects.exclude(Name='Harsh Sahu')

    # students = Student.objects.values('Name','Pass_date')            #esse only humko name and city ka dikhye ga aur agar koi value pass nhi krenge to dictionary return krega
    
    # students = Student.objects.values_list('id','city')               #esse only tuple ke form me ayega but dikhega nhi.
    # students = Student.objects.values_list('Roll','city',named=True)  #ab humko dikhega data

    #students = Student.objects.using('default')            # it tells which database we are using

    # students =Student.objects.dates('Pass_date','month')        #ye bhi terminal me dikhata h
    # students =Student.objects.datetimes('Pass_date','month')

    # qs1 = Student.objects.values_list('id','Name','city',named=True)
    # qs2 = Teacher.objects.values_list('id','Name','city',named=True)
    # students = qs1.union(qs2)
    #students = qs2.union(qs1)       #but yha duplicate nhi ayega
    # students = qs1.union(qs2,all=True)            #agar jada table h to qs1.union(qs2,qs3,qs4,all=True)

    # qs1 = Student.objects.values_list('Name',named=True)
    # qs2 = Teacher.objects.values_list('Name',named=True)
    # students = qs1.intersection(qs2)        # jo bhi data common h wo show krega only


    # qs1 = Student.objects.values_list('Name',named=True)
    # qs2 = Teacher.objects.values_list('Name',named=True)
    # students = qs1.difference(qs2)

    ############################################# AND OR OPERATOR #########################################

    # students = Student.objects.filter(id=6) & Student.objects.filter(Roll=6)
    # students = Student.objects.filter(id=6,Roll=6)
    # students = Student.objects.filter(Q(id=6) & Q(Roll=6))                #mostly used in this manner
    # students = Student.objects.filter(id=6) | Student.objects.filter(Roll=8)
    students = Student.objects.filter(Q(id=6) | Q(Roll=9))          #mostly used in this manner


    print('Sql Query:',students.query)          #to see the query in terminal
    return render(request,'school/home.html',{'student':students})