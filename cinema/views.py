from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie, Genre, Actor, Director
from django.template import loader

# Create your views here.
# index of the crud
def index(request):
    return HttpResponse("hello world")

# page of the movie

def movie(request, movie_id):
    results_list = Movie.objects.all()
    template = loader.get_template("cinema/movie_list.html")
    context = {
        'results' : results_list
    }
    for i in results_list:
        print(i)
    return HttpResponse(template.render(context, request))

# page of the genre
def genre(request, genre_id):
    return HttpResponse("genre name %s." % genre_id)

# page of the actor

def actor(request, actor_id):
    return HttpResponse("actor %s." % actor_id)

def director(request, director_id):
    return HttpResponse("director %s." % director_id)