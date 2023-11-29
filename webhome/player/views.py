from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect

from .models import Player


def index(request):
    context = {
        'players': Player.objects.all()
    }
    return render(request, 'player/index.html', context)


def get_player(request, player):
    print(player)
    if player == 'vadim':
        return redirect('home')

    return render(request, 'player/index.html', {'player': player})


def page_not_found(request, exception):
    return render(request, 'player/404.html', {'errors': exception})
