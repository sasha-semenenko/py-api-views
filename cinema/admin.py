from django.contrib import admin
from cinema.models import Movie, Actor, Genre, CinemaHall


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Actor)
class ACtorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    pass
