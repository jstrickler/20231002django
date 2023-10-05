"""Cookies! URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path, include
# from  someapp.views import some_view

# this is project level
urlpatterns = [
    path('admin/', admin.site.urls),
#    path('someview/', some_view),   # not the best practie, but *possible*
#   path('', include('welcome.urls', namespace='welcome')),
    path('', include('oreos.urls', namespace="oreos")),    # namespace:view
    # path('cc', include('chocchip.urls', namespace='chocchip')),  # {% url chocchip:home %}
    # add urls for apps here:
    # path('', include('my_app.urls', namespace="my_app")),
    # path('other_app', include('my_other_app.urls', namespace="other_app")),
]

# include Django Debug toolbar if DEBUG is set
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns