from django.contrib import admin
from .models import Author,Book,Post

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]