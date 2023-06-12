from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='user_login')
def crear_actividad(request):
    return render(request, 'main/crear_actividad.html')

@login_required(login_url='user_login')
def ver_actividad(request, resultado_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividades = resultado.actividad_set.all()
    return render(request, 'main/ver_actividad.html', {'resultado': resultado, 'actividades': actividades,})

@login_required(login_url='user_login')
def eliminar_resultado(request, resultado_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    if request.method == 'POST':
        resultado.delete()
        return redirect('home')
    return render(request, 'main/resultado/eliminar_resultado.html', {'resultado': resultado})


@login_required(login_url='user_login')
def modificar_resultado(request, resultado_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    if request.method == 'POST':
        resultado.nombre = request.POST.get('nombre')
        resultado.texto = request.POST.get('texto')
        resultado.save()
        return redirect('home')
    return render(request, 'main/resultado/modificar_resultado.html', {'resultado': resultado})


# @login_required(login_url='user_login')
# def modificar_resultado(request, resultado_id):
#     resultado = get_object_or_404(Resultado, id=resultado_id)
#     if request.method == 'POST':
#         form = ResultadoForm(request.POST, instance=resultado)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ResultadoForm(instance=resultado)
#     return render(request, 'main/resultado/modificar_resultado.html', {'form': form,})
        
    

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

    return render(request, 'main/resultado/crear_resultado.html', {'form': form, 'fecha_actual': fecha_actual,})

@login_required(login_url='user_login')
def home(request):
    resultados = Resultado.objects.all()
    return render(request, 'main/resultado/home.html', {'resultados':resultados,})

@login_required(login_url='user_login')
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.user.is_authenticated:
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
    

