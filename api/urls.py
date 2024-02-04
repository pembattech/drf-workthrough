from django.urls import path

from .views import api_home, api_home_post

urlpatterns = [
    path('', api_home, name = "api_home"),
    path('api_home_post', api_home_post, name = "api_home_post"),
]