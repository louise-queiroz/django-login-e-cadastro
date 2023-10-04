from django.contrib import admin
from django.urls import path
from app_login_usuario import views

urlpatterns = [
    #rota, view responsável, nomed e refência
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
