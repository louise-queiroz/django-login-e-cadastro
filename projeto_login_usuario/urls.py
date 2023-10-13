from django.contrib import admin
from django.urls import path, include
from app_login_usuario import views

urlpatterns = [
    #rota, view responsável, nomed e refência
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastropage'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('index/', views.login, name='index'),
    path('reset/', views.reset, name='reset')
]
