from django.urls import include, path
from signup import views

urlpatterns = [
    path('',views.users, name='signup_page_view'),
]
