from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=50,blank=True)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
        # return self.Name,self.Email ----> esse krne se name ke bagal me hi email aajayega but koi profit 
        # nhi h abhi to