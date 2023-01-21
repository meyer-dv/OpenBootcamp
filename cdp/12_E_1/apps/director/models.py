from django.db import models
from django.core.validators import URLValidator
from apps.movie.models import Movie


class Director(models.Model):
    GENDER_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    ]

    picture = models.URLField(
        validators=[URLValidator()],
        help_text="URL de la foto del director",
    )

    first_name = models.CharField(
        help_text="Nombre",
        max_length=255,
    )

    last_name = models.CharField(
        help_text="Apellidos",
        max_length=255,
    )

    birth_date = models.DateField(
        help_text="Fecha de nacimiento",
        blank=True,
        null=True,
    )

    birth_country = models.CharField(
        help_text="Lugar de nacimiento",
        max_length=50,
        blank=True,
        null=True,
    )

    sex = models.CharField(
        choices=GENDER_CHOICES,
        help_text="Sexo",
        max_length=1,
    )

    biography = models.TextField(
        max_length=500,
        help_text="Información sobre la carrera del director",
        blank=True,
        null=True,
    )

    movies = models.ManyToManyField(
        Movie,
        help_text="Películas",
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
