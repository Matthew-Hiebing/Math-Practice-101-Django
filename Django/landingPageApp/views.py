from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
import random

# Create your views here.

def landing_page_html(request):
    return render(request, 'landing_page.html')

def game_html(request):
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    problemResult = num1 * num2

    return render(request, 'game.html', {"problemResult" : problemResult})

