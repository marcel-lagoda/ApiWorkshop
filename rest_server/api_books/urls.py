from django.urls import path

from . import views

urlpatterns = [
    path('api/book/', views.BookList.as_view()),
    path('api/book/<int:id>', views.BookView.as_view()),
]