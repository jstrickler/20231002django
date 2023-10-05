"""
URL Configuration for oreos
"""
from django.urls import path
from . import views   # import views from app

app_name = "oreos"

urlpatterns = [
    # add url patterns for the oreos app here

    # Examples:
    path('', views.home, name='home'),
    path('dunk/', views.dunk, name='page2'),
    # path('thing', views.thing, name='thing'),
]
