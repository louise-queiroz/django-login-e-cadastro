from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar dados 
    novo_usuario = Usuario()
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    #exibir os dados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados
    return render(request,'usuarios/usuarios.html', usuarios)