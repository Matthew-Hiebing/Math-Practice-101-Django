from django.urls import path
from scores.views import scores

urlpatterns = [
    path('', scores, name='scores'),
]
