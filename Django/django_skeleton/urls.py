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
from django.urls import path
from django.conf.urls import include
from landingPageApp import views # 'langingPageApp' can also be replaced by '.' indicating that the folder is in the same directory.


urlpatterns = [
    # path('', views.return_html, name='landingPage-view'), # calls return_html function in views.py file.
    path('', include('landingPageApp.urls')), # Redirects you from "http://127.0.0.1:8000/" to "http://127.0.0.1:8000/homepage"
    path('admin/', admin.site.urls, name='admin-page-view'),
    # path('', views.return_html, name='main-view'),
    # path('',views.index,name='main-view'),

]
