from django.db import models

# Create your models here.
class Students(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=20)
    stuemail = models.EmailField(max_length=50)
    stupass = models.CharField(max_length=20)

    def __str__(self):
        return self.stuname