from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]