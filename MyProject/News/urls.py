from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contato/', views.contato, name="contato"),
    path('detalhes/', views.news_detalhes, name="detalhes"),
    path('year/<int:year>', views.news_anual, name="news_anual"),
    path('registro', views.registro, name="add"),
    path('add', views.addUser, name="addUser"),
]