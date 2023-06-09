from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='user_login')
def crear_resultado(request):
    fecha_actual = timezone.now()
    if request.method == 'POST':
        form = ResultadoForm(request.POST)
        if form.is_valid():
            resultado = form.save()
            return redirect('home')
    else:
        form = ResultadoForm

    return render(request, 'main/crear_resultado.html', {'form': form, 'fecha_actual': fecha_actual,})

@login_required(login_url='user_login')
def home(request):
    resultados = Resultado.objects.all()
    return render(request, 'main/home.html', {'resultados':resultados,})

@login_required(login_url='user_login')
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.user.is_authenticated:
        #redirige al usuario a la página correspondiente si ya ha iniciado sesión
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'login/login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/login.html', {'form': AuthenticationForm,'error': 'El nombre de usuario o contraseña son incorrectos'})
        else:
            login(request, user)
            return redirect('home')
    

