from django.urls import path
from scores.views import request_score_details

urlpatterns = [
    path('', request_score_details, name='request score details'),
]
