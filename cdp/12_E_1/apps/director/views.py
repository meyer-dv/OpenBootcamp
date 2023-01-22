from django.views.generic import ListView
from .models import Director


class home(ListView):
    model = Director
    template_name = "director/index.html"
