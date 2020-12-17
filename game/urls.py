from django.urls import path
from game.views import game

urlpatterns = [
    path('', game, name='game'),
]
