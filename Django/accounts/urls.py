from django.urls import include, path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/$',views.signup_view,name='signup'),
]
