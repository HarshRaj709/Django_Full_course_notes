from django.shortcuts import render
from django.db.models import Count
from .models import Student

# Create your views here.
def home(request):
    # students = Student.objects.get(pk=1)                      #work only for unique data
    # students = Student.objects.get(Name='Shristi Verma')

    # students = Student.objects.first()                          #first entry return kr rha h.
    # students = Student.objects.order_by('Name').first()        

    # students = Student.objects.last() 
    # students =Student.objects.filter(city='lucknow').last()         #ye city me jiske lucknow h usko return de rha h.             

    # students = Student.objects.latest('Roll')           #last modified data deta h esse.

    # students = Student.objects.earliest('Roll')
    # students = Student.objects.earliest('Pass_date')

    # students = Student.objects.filter(Name='Harsh Sahu').exists()       #returns True
    # students = Student.objects.filter(pk=12).exists()                       # retuns False

    # students = Student.objects.filter(pk=2).update(Name='Shristi Verma')        #yha pe get krke update nhi kr sakte h, filter krna hoga.
    # students = Student.objects.filter(Marks__lt=70).update(city='fail')     #ye humko return krta h ki kitne dataset 
        #  update hue h na ki ki Queryset return krta h to hum isko dekh nhi sakkte h apne templates me.
    # students,created = Student.objects.update_or_create(
    #     Name = 'Tushari jain',
    #     defaults={'Roll':113,'city':'mehmodabad','Marks':45,'Pass_date':'2023-10-14'}
    #     )           # Tushari jain ke naam se koi bhi data nhi tha to ye create ho gya..
    # print(created)


    # students = Student.objects.create(Name='Sameer',Roll=111,city='lucknow',Marks=60,Pass_date='2020-5-4') #data created and inserted in database.

    # students,created = Student.objects.get_or_create(Name='Ramadheer',Roll=112,city='lucknow',Marks=80,Pass_date='2020-10-4')
    # print(created)      #isme humko 2 things return kr rha h isiliye 2 variables me store krna hoga


    # students = Student.objects.bulk_create(
    #     [
    #         Student(Name='Shiva',Roll=117,city='lucknow',Marks=80,Pass_date='2020-5-24'),
    #         Student(Name='Sahkti',Roll=118,city='lakhimpur',Marks=100,Pass_date='2020-5-4')
    #     ]
    # )

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'Bhel'
    # students=Student.objects.bulk_update(all_student_data,['city'])

    # students = Student.objects.filter(Name='Mukesh').delete()
    # students = Student.objects.get(pk=12).delete()
    # students = Student.objects.filter(Marks__lt = 80).delete()
    # students = Student.objects.all().delete()       # to delete all data from database.


    # students=Student.objects.count()            #it returns 16 as there are 16 tuples in our database
    students=Student.objects.filter(Marks__lt=90).count()  #it returns11


    # print('Sql Query:',students.query)          #to see the query in terminal
    return render(request,'school/home.html',{'student':students})