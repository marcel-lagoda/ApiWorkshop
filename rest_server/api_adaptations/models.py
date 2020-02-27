from django.db import models
from api_books.models import Book

ACTION = 1
COMEDY = 2
CRIME = 3
INDEPENDENT = 4
DOCUMENTARY = 5
DRAMA = 6
WAR = 7

GENRES = (
    (ACTION, 'Action'),
    (COMEDY, 'Comedy'),
    (CRIME, 'Crime'),
    (INDEPENDENT, 'Independent'),
    (DOCUMENTARY, 'Documentary'),
    (DRAMA, 'Drama'),
    (WAR, 'War'),
)


class Movie(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    date = models.DateField()
    genre = models.CharField(max_length=21, choices=GENRES)

    def __str__(self):
        return self.title
