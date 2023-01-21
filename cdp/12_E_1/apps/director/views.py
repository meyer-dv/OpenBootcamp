from django.shortcuts import render
from .models import Director


def home(request):
    directors = Director.objects.all()

    context = {
        "directors": directors,
    }

    return render(request, "director/index.html", context)
