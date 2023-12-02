from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)

    def Authors(self):
        return ','.join([str(au) for au in self.author.all()])      # .join()   list[] ke elements join

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=50)
    song_duration = models.IntegerField()

    def singers(self):
        return ','.join([str(p) for p in self.user.all()])      #isme hum phle sare users get kr le rhe,phir unko string me convert krke unke bich me ',' lgwa ke return kr de rhe h. 