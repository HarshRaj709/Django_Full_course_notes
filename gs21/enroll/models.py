from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=10)
    stuemail = models.EmailField(max_length=20)
    stupass = models.CharField(max_length=20)

    def __str__(self):
        return self.stuname
    
class Teacher(models.Model):
    techid = models.IntegerField()
    techname = models.CharField(max_length=10)
    techmail = models.CharField(max_length=20)
    techpass = models.CharField(max_length=22)

    def __str__(self):
        return str(self.techid)
    
class college(models.Model):
    collegeid = models.IntegerField()
    collegename= models.CharField(max_length=50)
    collegeemail = models.CharField(max_length=90)
    collegepass = models.CharField(max_length=50)

    def __str__(self):
        return self.collegename
