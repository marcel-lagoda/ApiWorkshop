from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_books.urls')),
    path('', include('api_adaptations.urls')),
]
