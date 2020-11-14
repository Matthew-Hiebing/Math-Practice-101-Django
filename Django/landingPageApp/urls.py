from django.urls import path
from landingPageApp import views

urlpatterns = [
    path('', views.landing_page_html, name='landingPage-view'), # calls return_html function in views.py file.
    path('game/',views.game_html, name='gamePage-view'),
]
