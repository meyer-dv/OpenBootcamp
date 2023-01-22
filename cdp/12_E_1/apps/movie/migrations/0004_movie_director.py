# Generated by Django 4.1.5 on 2023-01-22 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("director", "0006_remove_director_movies"),
        ("movie", "0003_alter_movie_duration"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(
                default=None, on_delete=django.db.models.deletion.CASCADE, to="director.director"
            ),
            preserve_default=False,
        ),
    ]
