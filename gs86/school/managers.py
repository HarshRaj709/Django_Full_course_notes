from django.db import models
from django.db.models.query import QuerySet

class CustomManager(models.Manager):
    def get_queryset(self):                     #to override the get_queryset
        return super().get_queryset().order_by('name')
    