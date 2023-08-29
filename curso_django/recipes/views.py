from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# O Django é inteligente já para buscar o arquivo dentro da pasta templates
def home(request):
    return render(request, "recipes/home.html")


def sobre(request):
    return HttpResponse("Hello World!")


def contato(request):
    return HttpResponse("Hello World!")
