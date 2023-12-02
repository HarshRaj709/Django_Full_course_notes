from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    # date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
    
class Student(CommonInfo):
    student_id = models.IntegerField()
    fees_Submited = models.IntegerField()
    date = None

class Teacher(CommonInfo):
    Teachers_id = models.IntegerField()
    Salary = models.IntegerField()
    # date = models.DateTimeField()