# Generated by Django 4.1.5 on 2023-01-22 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("director", "0005_alter_director_movies"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="director",
            name="movies",
        ),
    ]
