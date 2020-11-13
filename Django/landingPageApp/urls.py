from django.urls import path
from landingPageApp import views

urlpatterns = [
    path('', views.test, name='landingPage-view'), # calls return_html function in views.py file.
    path('game/',views.return_html, name='gamePage-view'),
]
