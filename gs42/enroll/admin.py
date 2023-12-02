from django.contrib import admin
from .models import registration

# Register your models here.

@admin.register(registration)
class Regi(admin.ModelAdmin):
    list_display=['id','Name','Email','Password']