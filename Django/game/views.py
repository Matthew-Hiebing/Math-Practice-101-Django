from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import random

def game(request):
    return render(request, 'game/game.html')
