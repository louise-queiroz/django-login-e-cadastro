from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request,'usuarios/home.html')


def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

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

def logar_usuario(request):
    if request.method == "POST":
        email = request.POST["email"]  
        senha = request.POST["senha"]  
        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
    
    form_login = AuthenticationForm()
    return render(request, 'usuarios/cadastro.html', {'form_login': form_login})

def reset(request):
    return render(request, 'usuarios/reset.html')