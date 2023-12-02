from django.contrib import admin
from .models import userdata

# Register your models here.
@admin.register(userdata)
class usertable(admin.ModelAdmin):
    list_display = ['username','userId','userpassword']
#admin.site.register(userdata)