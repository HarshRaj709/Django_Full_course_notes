from django.contrib import admin
from .models import UserModel
# Register your models here.

# admin.site.register(UserModel)
@admin.register(UserModel)
class UserForm(admin.ModelAdmin):
    list_display=['id','Name','Email','Password']
    

