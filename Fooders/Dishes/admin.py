from django.contrib import admin
from .models import Recipe,Ingridents

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id','user','ingri','recipe_name','instructions']

@admin.register(Ingridents)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ingridents._meta.fields]