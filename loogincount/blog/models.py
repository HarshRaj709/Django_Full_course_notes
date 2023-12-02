from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField(max_length=100)    #esse TextArea ke jesa field ayega

    def __str__(self):
        return self.Title