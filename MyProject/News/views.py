from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao curso de Django")