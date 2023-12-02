from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ingridents(models.Model):
    user  = models.ForeignKey(to=User,on_delete=models.CASCADE)         #1 Chef can use multiple Ingridents one-to-many relationship 
    Spices_name = models.CharField(max_length=50)
    Spice_qunatity = models.IntegerField()

    def __str__(self):
        return self.Spices_name
    
class Recipe(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)     #many cheif can make 1 recipe or 1 chief can make many recepy
    ingrident = models.ManyToManyField(to=Ingridents)                   #many ingridents can be used on many Recepies
    recipe_name = models.CharField(max_length=70)
    instructions = models.TextField()

    def ingri(self):
        return ','.join([str(name) for name in self.ingrident.all()])