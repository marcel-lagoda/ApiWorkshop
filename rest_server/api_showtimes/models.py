from django.db import models

from api_adaptations.models import Movie


class Cinema(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    movies = models.ManyToManyField(Movie, through='Screening')


class Screening(models.Model):
    date = models.DateField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
