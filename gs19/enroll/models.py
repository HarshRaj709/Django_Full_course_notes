from django.db import models

# Create your models here.
class hostel(models.Model):
    hostel_room = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=50)
    stu_age = models.IntegerField()