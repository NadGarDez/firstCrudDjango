from django.contrib import admin
from .models import Actor, Movie, Director, Genre
# Register your models here.

admin.site.register([Actor, Movie,Director, Genre])