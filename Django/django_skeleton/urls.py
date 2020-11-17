"""django_skeleton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from landing_page_app import views # 'langingPageApp' can also be replaced by '.' indicating that the folder is in the same directory.


urlpatterns = [
    path('', views.landing_page, name='landing_page_view'),
    path('admin/', admin.site.urls, name='admin_page_view'),
    path('game/',views.game, name='game_page_view'),
    path('registration/',views.users, name='registration_page_view'),
]
