from django.shortcuts import render
def index(request):
    context = {
        "nome" : "vinicius"
    }
    return recdnder(request, 'home.html', context)