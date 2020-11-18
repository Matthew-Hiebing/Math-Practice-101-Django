from django.urls import include, path
from game import views

urlpatterns = [
    path('',views.game_logic, name='game'),
]
