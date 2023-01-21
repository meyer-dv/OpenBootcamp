# Generated by Django 4.1.5 on 2023-01-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0002_alter_movie_duration_alter_movie_poster_and_more"),
        ("director", "0004_alter_director_biography_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="director",
            name="movies",
            field=models.ManyToManyField(blank=True, help_text="Películas", to="movie.movie"),
        ),
    ]
