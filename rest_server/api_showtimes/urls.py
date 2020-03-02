from django.urls import path

from . import apiviews

urlpatterns = [
    path('cinemas/', apiviews.CinemaList.as_view()),
    path('cinemas/<int:id>', apiviews.CinemaView.as_view()),
    path('screenings', apiviews.ScreeningList.as_view()),
    path('screenings/<int:id>', apiviews.ScreeningView.as_view()),
]
