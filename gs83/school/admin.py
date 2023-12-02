from django.contrib import admin
from .models import Student,Examcenter

# Register your models here.
@admin.register(Examcenter)
class Examcenteradmin(admin.ModelAdmin):
    list_display = [field.name for field in Examcenter._meta.fields]

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]