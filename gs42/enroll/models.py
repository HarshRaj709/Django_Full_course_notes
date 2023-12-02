from django.db import models

# Create your models here.
class registration(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.Name