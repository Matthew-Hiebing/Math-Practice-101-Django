from django.urls import path
from landingPageApp import views

urlpatterns = [
    path('', views.return_html, name='landingPage-view'), # calls return_html function in views.py file.
    # path('', views.index, name='main-view'),
]
