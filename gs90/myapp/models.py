from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name                #Bus humko yhi se name return krdena h author ka to humko book section me dekhne ko mil jayega Author name.

class Book(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(to=Author,on_delete=models.CASCADE)

class Post(models.Model):
    # user = models.ForeignKey(to=User,on_delete=models.CASCADE)          #foreignkey se humara many-to-one reationship bnti h.
    # user = models.ForeignKey(to=User,on_delete=models.PROTECT)      #agar hum chate h ki user tb tk delete na ho jabtk uski sari post delete na ho jaye.

    # abhi hum chate h ki user ke delete hone ke bad bhi humara post delete na ho.
    user = models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True)   #agar humko SET_NULL krna h to humko null=True bhi set krna hoga.phir humko migrate krna hoga.
    post_title = models.CharField(max_length=50)
    post_cat = models.CharField(max_length=50)
    post_publish_data = models.DateField(auto_now_add=True)

