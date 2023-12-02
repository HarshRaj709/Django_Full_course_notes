from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','Title','Description']