# Generated by Django 4.1.5 on 2023-01-21 20:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(help_text="Título de la película", max_length=100)),
                (
                    "poster",
                    models.URLField(
                        help_text="URL de la portada de la película",
                        validators=[django.core.validators.URLValidator()],
                    ),
                ),
                ("imdb_rating", models.FloatField(help_text="Calificación IMDb", max_length=4)),
                ("synopsis", models.TextField(help_text="Sinopsis", max_length=500)),
                ("release_date", models.DateField(help_text="Fecha de lanzamiento")),
                ("duration", models.TimeField()),
                (
                    "trailer",
                    models.URLField(
                        help_text="URL del trailer de la película",
                        validators=[django.core.validators.URLValidator()],
                    ),
                ),
                (
                    "genres",
                    models.ManyToManyField(help_text="Género de la película", to="movie.genre"),
                ),
            ],
        ),
    ]
