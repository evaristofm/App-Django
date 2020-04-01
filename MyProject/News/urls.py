from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contato/', views.contato, name="contato"),
    path('detalhes/', views.news_detalhes, name="detalhes"),
]