from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class User(models.Model):

class Page(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE,primary_key=True)
    # user = models.OneToOneField(to=User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True}) #ab only jo staff h wahi create kr sakta h 
    # user = models.OneToOneField(to=User,on_delete=models.PROTECT,primary_key=True)  #agar isko humne PROTECT kr 
    #diya to hum directly user ko delete nhi kr sakte h jo bhi isse associated h. phle humko page delete krna hoga.
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
        