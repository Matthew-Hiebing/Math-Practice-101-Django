from django.urls import path
from landingPageApp import views

urlpatterns = [
    path('',views.index,name='index'),
]
