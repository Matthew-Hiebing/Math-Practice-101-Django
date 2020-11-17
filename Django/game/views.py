from django.shortcuts import render
import random

# Create your views here.
def game_logic(request):
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    problemResult = num1 * num2
    return render(request, 'game/game.html', {"problemResult": problemResult})
