from django.contrib import admin
from .models import students

# Register your models here.
@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ('stuid','stuname','stuemail','stupass')

# admin.site.register(students,studentsAdmin)