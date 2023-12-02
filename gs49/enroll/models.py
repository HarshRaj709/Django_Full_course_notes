from django.db import models

# Create your models here.
class User(models.Model):
    Student_name = models.CharField(max_length=50)
    Teacher_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)