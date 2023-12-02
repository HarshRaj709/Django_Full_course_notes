from django.db import models
from django.db.models.query import QuerySet

class CustomManager(models.Manager):
    def get_roll(self,r1,r2):
        return super().get_queryset().filter(roll__range=[r1,r2])
    