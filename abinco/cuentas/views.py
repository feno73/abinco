from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import FormularioCreacionUsuario, FormularioInicioSesion
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError

def cuentas(request):
    if request.user.is_authenticated:
        return redirect('/inventario')
    else:
        return redirect('iniciarsesion')

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {'form':FormularioCreacionUsuario})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inventario')
            except IntegrityError:
                return render(request, 'registrarse.html', {'form': FormularioCreacionUsuario, 'error':'El nombre de usuario ya existe'})    
        else:
            return render(request, 'registrarse.html', {'form': FormularioCreacionUsuario, 'error':'Las contraseñas no coinciden'})

def iniciarsesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarsesion.html', {'form': FormularioInicioSesion})
    else:
        user = authenticate(request, username=request.POST['username'], password= request.POST['password'])
        if user is None:
            return render(request, 'iniciarsesion.html', {'form': FormularioInicioSesion(), 'error': 'El usuario o la contraseña son incorrectos'})
        else:
            login(request, user)
            return redirect('/inventario')

def cerrarsesion(request):
    logout(request)
    return redirect('iniciarsesion')

