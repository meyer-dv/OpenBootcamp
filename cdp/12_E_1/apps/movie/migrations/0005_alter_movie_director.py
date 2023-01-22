# Generated by Django 4.1.5 on 2023-01-22 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("director", "0006_remove_director_movies"),
        ("movie", "0004_movie_director"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(
                default=None, on_delete=django.db.models.deletion.CASCADE, to="director.director"
            ),
        ),
    ]
