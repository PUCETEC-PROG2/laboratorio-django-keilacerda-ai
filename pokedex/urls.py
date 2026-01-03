from django.urls import path
from . import views

app_name = "pokedex"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('pokemon/<str:pokemon_name>/', views.pokemon, name="pokemon_details"),
    path("add/", views.add_pokemon, name="add_pokemon"),
    path("edit/<str:pokemon_name>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete/<str:pokemon_name>/", views.delete_pokemon, name="delete_pokemon"),
]

