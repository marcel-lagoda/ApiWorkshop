from django.contrib import admin

from . import models
from api_adaptations.models import Movie


class CinemaInline(admin.TabularInline):
    model = models.Cinema.movies.through


class CinemaAdmin(admin.ModelAdmin):
    model = Movie
    inlines = [CinemaInline]


admin.site.register(models.Cinema, CinemaAdmin)
# admin.site.register(models.Movie)
admin.site.register(models.Screening)
