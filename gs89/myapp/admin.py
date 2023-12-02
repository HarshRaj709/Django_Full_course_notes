from django.contrib import admin
from .models import Page,like

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Page._meta.fields]

@admin.register(like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in like._meta.fields]