from django.http import HttpResponse
from django.shortcuts import render
from .models import Pokemon

def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {
    'pokemons': pokemons
})

def pokemon_details(request, pokemon):
    pokemon_obj = Pokemon.objects.get(name=pokemon)
    return render(request, 'pokemon_details.html', {
        'pokemon': pokemon_obj
    })
