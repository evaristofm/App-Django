from django.shortcuts import render, HttpResponse, redirect
from .models import News, SportNews, Registro
from .forms import RegistroForm


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

def news_anual(request, year):
    list = News.objects.filter(pub_date__year=year)
    context = {
        'year': year,
        'arquivo_list': list
    }
    return render(request, 'news_anual.html', context)


def registro(request):
    context = {"form": RegistroForm}
    return render(request, 'registro.html', context)

def addUser(request):
    form = RegistroForm(request.POST)
    if form.is_valid():
        registro = Registro(user_name=form.cleaned_data['user_name'],
                            password=form.cleaned_data['password'],
                            email=form.cleaned_data['email'],
                            phone=form.cleaned_data['phone'])
        registro.save()
        return redirect('/')

