from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'book', 'title', 'director', 'date', 'genre')