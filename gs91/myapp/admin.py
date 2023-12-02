from django.contrib import admin
from .models import Author,Book,Song

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','title','Authors'] 

@admin.register(Song)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','song_name','song_duration','singers']    