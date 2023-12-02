from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]