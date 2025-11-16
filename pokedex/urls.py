from django.urls import path
from . import views
from .views import trainer_list

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:pokemon>/", views.pokemon_details, name="pokemon_details"),
    # Trainer
    path("trainer/", views.trainer_list, name="trainer_list"),
    path("trainer/<int:trainer_id>/", views.trainer_details, name="trainer_details"),
]
