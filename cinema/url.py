from django.urls import path
from . import views


urlpatterns = [
    path("", views.index , name="index"), # print some movies , actors, and genres, and directors
    path("movie/<int:movie_id>/", views.movie, name="movie"),
    path("movies/", views.movies, name="movies"),
    path("actor/<int:actor_id>/", views.actor, name="actor"),
    path("actors/", views.actors, name="actors"),
    path("director/<int:director_id>/", views.director, name="director"),
    path("directors/", views.directors, name="directors"),
    path("genre/<int:genre_id>/", views.genre, name="genre"),
    path("genre/form/", views.genre_form, name="set_genre"),
    path("search/<str:search>/<str:category>/", view=views.search, name="search"),
    path("success_screen/<str:title>/<str:subtitle>",view=views.success_screen,name="success" ),
    path("save_genre",view=views.save_genre, name="save_genre")
]