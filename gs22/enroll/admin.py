from django.contrib import admin
from .models import Students
# Register your models here.

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','stuname','stuemail','stupass','stuid')


# admin.site.register(Students,StudentAdmin)