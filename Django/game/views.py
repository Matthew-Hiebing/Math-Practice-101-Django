from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
@login_required(login_url="/accounts/login/")
def game_logic(request):
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    problemResult = num1 * num2
    return render(request, 'game/game.html', {"problemResult": problemResult})
