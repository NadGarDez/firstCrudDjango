from django.test import TestCase
from .models import Movie, Genre, Award, Director, Actor
import datetime

class TestMovie(TestCase):

    def setUp(self) -> None:

        # genre

        genre = Genre()
        genre.name = "drama"
        genre.save()

        # awards 

        award = Award()
        award.name = "Oscar"
        award.save()

        # director 

        director = Director()
        director.name = "director"
        director.actor_image = "www.google.com/image"
        director.actor_resume = "resume"
        director.save()
        

        #actor 

        actor = Actor()
        actor.name = "actor"
        actor.actor_image = "www.google.com/image"
        actor.actor_resume = "resume"
        actor.save()

        movie = Movie()
        movie.name = "some name"
        movie.pk = 1
        movie.synopsis = "some synopsis"
        movie.premiere = datetime.datetime(2023, 2,2)
        movie.image = "www.google.com/image"
        movie.director = director
        movie.genre.set([genre])
        movie.actors.set([actor])
        movie.awards.set([award])
        movie.save()

        return super().setUp()
    
    def test_has_awards_function(self):
        movie = Movie.objects.get(name ="some name")
        self.assertEqual(movie.has_awards(), True)