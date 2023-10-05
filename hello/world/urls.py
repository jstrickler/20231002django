from django.urls import path
from . import views
# from . import other_views
# from . import more_views

app_name = "world"

urlpatterns = [
    path('/', views.home, name='home'),
]
