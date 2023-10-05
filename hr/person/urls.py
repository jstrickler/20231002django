"""
URL Configuration for person
"""
from django.urls import path
from . import views   # import views from app

app_name = "person"

urlpatterns = [
    # add url patterns for the person app here

    # Examples:
    path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
