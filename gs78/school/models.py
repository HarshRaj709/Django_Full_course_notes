from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=50)
    Roll = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=70)
    Marks = models.IntegerField()
    Pass_date = models.DateField()

class Teacher(models.Model):
    Name = models.CharField(max_length=50)
    empnum = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()