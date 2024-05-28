from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "todos/home.html")
    # return HttpResponse("Hello, Treining!")


# Create your views here.
