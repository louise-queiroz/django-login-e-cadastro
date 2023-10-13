from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from django.contrib import messages


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


def reset(request):
    return render(request, 'usuarios/reset.html')

def erro(request):

    messages.error(request, 'Não possível realizar o login.')
    return render(request, ('home'))


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            user = authenticate(request, email=email, senha=senha)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                erro()
        else:
            erro()
    else:
        form = LoginForm()

    return render(request, 'home', {'form': form})