from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home.html')

def contato(request):
    return render(request, 'contato.html')