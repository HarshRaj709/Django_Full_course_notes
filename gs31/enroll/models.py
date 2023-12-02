from django.db import models

# Create your models here.

class userdata(models.Model):
    userId = models.IntegerField()
    username = models.CharField(max_length=50)
    userpassword = models.CharField(max_length=50)

    def __str__(self):
        return self.username