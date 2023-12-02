from django.contrib import admin
from .models import student
# Register your models here.

@admin.register(student)
class studentModel(admin.ModelAdmin):
    list_display = ['stuid','stuname','stuemail','stupassword']