from django.db import models

# Create your models here.
class Examcenter(models.Model):
    cname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Student(Examcenter):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()