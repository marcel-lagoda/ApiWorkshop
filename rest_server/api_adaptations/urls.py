from django.urls import path

from . import apiviews

urlpatterns = [
    path('movies/', apiviews.MovieList.as_view()),
    path('movies/<int:id>', apiviews.MovieView.as_view()),
]
