from django.shortcuts import render, get_object_or_404
from apps.director.models import Director


def movies_by_director(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    movies = director.movies.all()
    return render(request, "movie/movies.html", {"movies": movies})
