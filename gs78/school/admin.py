from django.contrib import admin
from .models import Student,Teacher
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Roll','city','Marks','Pass_date']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','Name','empnum','city','salary','join_date']
