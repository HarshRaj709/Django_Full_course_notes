from django.contrib import admin
from .models import Topic,Entry

# Register your models here.
@admin.register(Topic)
class AdminTopic(admin.ModelAdmin):
    list_display = ['id','text','date_added']

@admin.register(Entry)
class AdminEntry(admin.ModelAdmin):
    list_display=[field.name for field in Entry._meta.fields]