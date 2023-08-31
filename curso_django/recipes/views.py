from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# O Django é inteligente já para buscar o arquivo dentro da pasta templates
def home(request):
    return render(request, "recipes/pages/home.html", context={
        'name': 'Luiz Otávio',
    })


def recipe(request, id):
    return render(request, "recipes/pages/recipe-view.html", context={
        'name': 'Luiz Otávio',
    })
