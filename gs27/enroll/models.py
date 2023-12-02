from django.db import models

# Create your models here.
class student(models.Model):
    stuid = models.IntegerField()
    stname = models.CharField(max_length=50)
    stemail = models.EmailField(max_length=60)

    def __str__(self):
        return self.stname
