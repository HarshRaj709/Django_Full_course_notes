from django.contrib import admin
from .models import Examcenter,MyExamcenter

# Register your models here.
@admin.register(Examcenter)
class ExamAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Examcenter._meta.fields]


@admin.register(MyExamcenter)
class MyExamAdmin(admin.ModelAdmin):
    list_display=[field.name for field in MyExamcenter._meta.fields]