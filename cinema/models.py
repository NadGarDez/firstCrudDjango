from django.db import models

# Create your models here.

class Actor(models.Model):
    name=models.CharField(max_length=100)
    actor_image = models.URLField(max_length=200, null=True)
    actor_resume = models.TextField(null=True)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Director(models.Model): 
    name=models.CharField(max_length=100)
    actor_image = models.URLField(max_length=200, null=True)
    actor_resume = models.TextField(null=True)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=50)
    synopsis = models.TextField()
    premiere = models.DateField()
    actors = models.ManyToManyField(Actor, related_name="related_actors")
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name="related_genre")
    image = models.URLField(max_length=250)
    def __str__(self):
        return self.name