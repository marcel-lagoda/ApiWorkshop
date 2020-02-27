from django.urls import path

from . import apiviews

urlpatterns = [
    path('movie/', apiviews.MovieList.as_view()),
]
