# Generated by Django 4.1.5 on 2023-01-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0002_alter_movie_duration_alter_movie_poster_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.IntegerField(help_text="Duración en minutos de la película"),
        ),
    ]
