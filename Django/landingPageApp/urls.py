from django.urls import path
from landingPageApp import views

urlpatterns = [
    # path('', views.index, name='main-view'),
    path('', views.index, name='main-view'),
]
