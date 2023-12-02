from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE,primary_key=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField(auto_now_add=True)

class like(Page):
    panna = models.OneToOneField(to=Page,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    likes = models.IntegerField()           #isme default hi 1to1 ka relationship hoga.