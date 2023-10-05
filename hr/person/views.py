from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Personnel")

