from rest_framework import serializers
from .models import Cinema, Screening

from api_adaptations.serializers import MovieSerializer


class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Cinema
        fields = ('name', 'city', 'movies')


class ScreeningSerializer(serializers.HyperlinkedModelSerializer):

    movie = MovieSerializer()
    cinema = CinemaSerializer()

    class Meta:
        model = Screening
        fields = ('movie', 'cinema', 'date')
