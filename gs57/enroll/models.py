from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)