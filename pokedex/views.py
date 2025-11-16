from django.http import HttpResponse
from django.shortcuts import render
from .models import Pokemon
from .models import Trainer

def index(request):
    pokemons = ['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle', 'Charizard']
    return render(request, 'index.html', {
    'pokemons': pokemons
})


def pokemon_details(request, pokemon):
    return render(request, 'pokemon_details.html', {
        'pokemon': pokemon
    })


def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_list.html', {
        'trainers': trainers
    })

def trainer_details(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    return render(request, 'trainer_details.html', {
        'trainer': trainer
    })

