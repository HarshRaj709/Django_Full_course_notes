from django.db import models

# Create your models here.
class student(models.Model):
    stuid = models.IntegerField(primary_key=True,)
    stuname = models.CharField(max_length=50,db_column='Name')
    stuemail = models.EmailField(max_length=100,db_column='Email')
    stupassword = models.CharField(max_length=50,db_column='Password')

    