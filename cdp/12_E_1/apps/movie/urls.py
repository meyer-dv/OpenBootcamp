from django.urls import path
from .views import movies_by_director


urlpatterns = [
    path("<pk>", movies_by_director.as_view(), name="movies_by_director"),
]
