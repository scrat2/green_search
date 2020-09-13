"""
URLs list for authentication app. Put different links here and they will be add in /kcalc/urls.py. It's only links for
pages which have a relation with the authentication.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add),
    path('', views.search),
]
