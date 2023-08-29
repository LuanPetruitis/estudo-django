from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("""
        <!DOCTYPE>
        <html>
            <head>
                <title> Olá mundo</title>
            </head>
            <body>
                Hello World!
            </body>
        <html>
    """)

def sobre(request):
    return HttpResponse("Hello World!")

def contato(request):
    return HttpResponse("Hello World!")