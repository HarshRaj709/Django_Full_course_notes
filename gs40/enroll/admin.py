from django.contrib import admin
from .models import Employee
# Register your models here.


# admin.site.register(Employee)
@admin.register(Employee)
class DispalyAdmin(admin.ModelAdmin):
    list_display=['Name','id','Email','Password']   # isme hum {name} nhi likh skte h jo display hota h 
     # name wahi likhna hota, {forms.py-->label} me humne Name diya h isiliye Name hi dena hoga