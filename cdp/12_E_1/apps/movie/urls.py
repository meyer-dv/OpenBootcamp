from django.urls import path
from . import views



urlpatterns = [
    path("<director_id>", views.movies_by_director, name="movies_by_director"),
]
