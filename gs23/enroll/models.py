from django.db import models

# Create your models here.
class students(models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField(max_length=50)
    stupass = models.CharField(max_length=50)

    def __str__(self):
        return self.stuname