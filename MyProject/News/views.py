from django.shortcuts import render, HttpResponse
from .models import News, SportNews


def home(request):
    return render(request, 'home.html')

def contato(request):
    return render(request, 'contato.html')

def news_detalhes(request):
    obj = News.objects.get(id=1)
    context = {
        "obj": obj
    }
    return render(request, 'news_detalhes.html', context)