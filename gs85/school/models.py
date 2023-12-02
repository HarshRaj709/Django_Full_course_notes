from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()

    # objects = models.Manager()            #ye default lga hua h jiski wajah se hum views.py me objects ke through access kr pate h.
    students = models.Manager()     #ab hum students ke name se acess kr payenge..