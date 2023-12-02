from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class Adminuser(admin.ModelAdmin):
    list_display = ['id','Name','Email','Password']