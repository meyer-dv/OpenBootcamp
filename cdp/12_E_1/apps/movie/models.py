from django.db import models
from django.core.validators import URLValidator


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Título de la película",
    )

    poster = models.URLField(
        validators=[URLValidator()],
        help_text="URL de la portada de la película",
        blank=True,
        null=True,
    )

    imdb_rating = models.FloatField(
        max_length=4,
        help_text="Calificación IMDb",
    )

    synopsis = models.TextField(
        max_length=500,
        help_text="Sinopsis",
        blank=True,
        null=True,
    )

    release_date = models.DateField(
        help_text="Fecha de lanzamiento",
        blank=True,
        null=True,
    )

    duration = models.IntegerField(
        help_text="Duración en minutos de la película",
    )

    genres = models.ManyToManyField(
        Genre,
        help_text="Género de la película",
    )

    trailer = models.URLField(
        validators=[URLValidator()],
        help_text="URL del trailer de la película",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title
