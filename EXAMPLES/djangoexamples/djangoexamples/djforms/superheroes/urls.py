"""
URL Configuration for djforms/superheroes
"""
from django.urls import path
from . import views

app_name = 'djforms'

urlpatterns = [
    path('', views.home, name='home'),
    path('demoform', views.demoform, name='demoform'),
    path('heroform', views.heroform, name='heroform'),
    path('heroadd', views.heroadd, name='heroadd'),
    path('herolist', views.herolist, name='herolist'),
    path('herodetails/<str:hero_name>', views.herodetails, name='herodetails'),
]

