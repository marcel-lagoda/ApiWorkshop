from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('book/<int:id>', views.BookView.as_view()),
]