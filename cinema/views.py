from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Movie, Genre, Actor, Director
from django.template import loader
from django.urls import reverse

# Create your views here.
# index of the crud
def index(request):
    try:
        result = Movie.objects.all()[:5]
    except Movie.director:
        raise Http404("There are not movies")
    
    template = loader.get_template("cinema/index.html")
    
    context = {
        'results': result
    }

    return HttpResponse(template.render(context, request))

# page of the movie

def movie(request, movie_id):
    try:
        result = Movie.objects.get(pk=movie_id)

    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")

    template = loader.get_template("cinema/movie.html")

    actors_query = result.actors.get_queryset()
    director_query = Director.objects.get(name=result.director)
    genre_query = result.genre.get_queryset()

    context = {
        'result' : result,
        'actors': actors_query,
        'actors_len': actors_query.count(),
        'director': director_query,
        'genres': genre_query, 
        'genres_len': genre_query.count()
    }
    return HttpResponse(template.render(context, request))

def movies(request):
    return HttpResponse("movies")

# page of the genre
def genre(request, genre_id):
    try:
        movieResult = Movie.objects.all().filter(genre=genre_id)
        genreResult = Genre.objects.get(pk=genre_id)
        
    except Genre.DoesNotExist:
        raise Http404("Actor does not exist")
    
    template = loader.get_template("cinema/genre.html")

    context = {
        'movie_result': movieResult,
        'genre_result': genreResult
    }

    return HttpResponse(template.render(context, request))
    

# page of the actor

def actor(request, actor_id):
    try:
        result = Actor.objects.get(pk=actor_id)
    except Actor.DoesNotExist:
        raise Http404("Actor does not exist")
    
    print(result)
    template = loader.get_template("cinema/actor.html")

    context = {
        'result': result
    }

    return HttpResponse(template.render(context, request))

def actors(request):
    return HttpResponse("Actors")
    


def director(request, director_id):
    try:
        result = Director.objects.get(pk=director_id)
    except Director.DoesNotExist:
        raise Http404("Director does not exist")
    template=loader.get_template("cinema/director.html")
    context = {
        'result':result
    }
    return HttpResponse(template.render(context, request))

def directors(request):
    return HttpResponse("Directors")

def search(request, search, category):
    return HttpResponse("Search in " + category + ": " + search)

def success_screen(request, title, subtitle):

    context= {
        "title": title,
        "subtitle":subtitle
    }

    template = loader.get_template("cinema/success.html")

    return HttpResponse(template.render(context,request))

def genre_form(request):
    template = loader.get_template("cinema/genre_form.html")

    return HttpResponse(template.render({},request))

def save_genre(request):
    try:
        genre = Genre()
        genre.name = request.POST["genre_name"]
        genre.save()
       
    except:
        return Http404("Error saving your genre")

    return HttpResponseRedirect(reverse("success",args=("Success", "Saved genre successfully")))
    


