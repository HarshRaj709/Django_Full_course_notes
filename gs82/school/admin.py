from django.contrib import admin
from .models import Student,Teacher

# Register your models here.
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display=[field.name for field in Student._meta.fields]

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display=[field.name for field in Teacher._meta.fields]