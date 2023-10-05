from django.shortcuts import render, HttpResponse

def my_not_a_view():
    pass


def home(request):
    x = my_not_a_view()
    return HttpResponse("Django is the bomb!")

