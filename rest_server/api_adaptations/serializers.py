from rest_framework import serializers
from api_books.serializers import BookSerializer
from .models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    book = BookSerializer()

    class Meta:
        model = Movie
        fields = ('book', 'title', 'director', 'date', 'genre')