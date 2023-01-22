from django.views.generic import ListView
from apps.movie.models import Movie


class movies_by_director(ListView):
    model = Movie
    template_name = "movie/movies.html"
