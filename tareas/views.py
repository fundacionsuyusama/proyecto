from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta

@login_required(login_url='user_login')
def eliminar_alternativa(request, resultado_id, actividad_id, dificultad_id, id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    alternativa = get_object_or_404(Alternativa, id=id)

    if request.method == 'POST':
        alternativa.delete()
        return redirect('ver_actividad', resultado_id=resultado_id)
    
    return render(request, 'main/alternativa/eliminar_alternativa.html', {'alternativa': alternativa, 'resultado': resultado, 'resultado_id': resultado_id})

@login_required(login_url='user_login')
def editar_alternativa(request, resultado_id, actividad_id, dificultad_id, id):
    alternativa = get_object_or_404(Alternativa, id=id)

    if request.method == 'POST':
        alternativa.contenido = request.POST.get('contenido')
        alternativa.save()
        return redirect('ver_actividad', resultado_id=resultado_id)

    return render(request, 'main/alternativa/editar_alternativa.html', {'alternativa': alternativa})

@login_required(login_url='user_login')
def crear_alternativa(request, resultado_id, actividad_id, dificultad_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividad = get_object_or_404(Actividad, id=actividad_id)
    dificultad = get_object_or_404(Dificultad, id=dificultad_id)

    if request.method == 'POST':
        contenido = request.POST['contenido']
        alternativa = dificultad.alternativa_set.create(contenido=contenido)
        alternativa.save()
        return redirect('ver_actividad', resultado_id=resultado.id)
    
    return render(request, 'main/alternativa/crear_alternativa.html', {'actividad': actividad, 'resultado': resultado})

@login_required(login_url='user_login')
def editar_dificultad(request, resultado_id, actividad_id, id):
    dificultad = get_object_or_404(Dificultad, id=id)

    if request.method == 'POST':
        dificultad.contenido = request.POST.get('contenido')
        dificultad.save()
        return redirect('ver_actividad', resultado_id=resultado_id,)
    
    return render(request, 'main/dificultad/editar_dificultad.html', {'dificultad': dificultad})

@login_required(login_url='user_login')
def crear_dificultad(request, resultado_id, actividad_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividad = get_object_or_404(Actividad, id=actividad_id)

    if request.method == 'POST':
        contenido = request.POST['contenido']
        dificultad = actividad.dificultad_set.create(contenido=contenido)
        dificultad.save()
        return redirect('ver_actividad', resultado_id=resultado.id)
    
    return render(request, 'main/dificultad/crear_dificultad.html', {'actividad': actividad, 'resultado': resultado})

@login_required(login_url='user_login')
def eliminar_dificultad(request, resultado_id, actividad_id, id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    dificultad = get_object_or_404(Dificultad, id=id)

    if request.method == 'POST':
        dificultad.delete()
        return redirect('ver_actividad', resultado_id=resultado_id)
    
    return render(request, 'main/dificultad/eliminar_dificultad.html', {'dificultad': dificultad, 'resultado':resultado, 'resultado_id': resultado_id})

@login_required(login_url='user_login')
def eliminar_avance(request, resultado_id, actividad_id, id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    avance = get_object_or_404(Avance, id=id)

    if request.method == 'POST':
        avance.delete()
        return redirect('ver_actividad', resultado_id=resultado_id)
    
    return render(request, 'main/avance/eliminar_avance.html', {'avance': avance, 'resultado': resultado, ' resultado_id': resultado_id,})

@login_required(login_url='user_login')
def editar_avance(request, resultado_id, actividad_id, id):
    avance = get_object_or_404(Avance, id=id)
    
    if request.method == 'POST':
        avance.contenido = request.POST.get('contenido')
        avance.save()
        return redirect('ver_actividad', resultado_id=resultado_id,)
    
    return render(request, 'main/avance/editar_avance.html', {'avance': avance})

@login_required(login_url='user_login')
def crear_avance(request, resultado_id, actividad_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividad = get_object_or_404(Actividad, id=actividad_id)

    if request.method == 'POST':
        contenido = request.POST['contenido']
        avance = actividad.avance_set.create(contenido=contenido)
        avance.save()
        return redirect('ver_actividad', resultado_id=resultado.id)
    
    return render(request, 'main/avance/crear_avance.html', {'actividad': actividad, 'resultado': resultado})


@login_required(login_url='user_login')
def guardar_seccion(request, resultado_id, actividad_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividad = get_object_or_404(Actividad, id=actividad_id)
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('seccion_'):
                seccion_id = key.split('_')[-1]
                seccion_status = value
                try:
                    seccion = Seccion.objects.get(id=seccion_id)
                    seccion.is_completed = (seccion_status == "completed")
                    seccion.save()
                except Seccion.DoesNotExist:
                    pass

    return redirect('ver_secciones', resultado_id=resultado_id, actividad_id=actividad_id)

@login_required(login_url='user_login')
def ver_secciones(request, resultado_id, actividad_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividad = get_object_or_404(Actividad, id=actividad_id)
    secciones = actividad.seccion_set.all()
    total_secciones = secciones.count()

    actividad_actual = actividad.fecha_vencimiento

    fecha_actual = datetime.now().date()
    diferencia_tiempo = actividad_actual.date() - fecha_actual

    if total_secciones != 0:
        resultado_fecha = diferencia_tiempo / total_secciones
    else:
        resultado_fecha = 0

    secciones_completadas = sum(seccion.is_completed for seccion in secciones)

    if total_secciones > 0:
        porcentaje = round((secciones_completadas / total_secciones) * 100)
        total_porcentaje = round(100 / total_secciones)
    else:
        porcentaje = 0
        total_porcentaje = 0

    return render(request, 'main/secciones/ver_secciones.html', {'resultado': resultado, 'actividad': actividad, 'secciones': secciones, 'actividad_id': actividad_id, 'total_secciones': total_secciones, 'secciones_completadas': secciones_completadas, 'porcentaje': porcentaje, 'resultado_id': resultado_id, 'total_porcentaje': total_porcentaje, 'actividad_actual': actividad_actual, 'resultado_fecha': resultado_fecha, 'resultado_fecha': resultado_fecha, 'nav': True,})

@login_required(login_url='user_login')
def eliminar_secciones(request, resultado_id, actividad_id, id):
    seccion = get_object_or_404(Seccion, id=id)
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividad = get_object_or_404(Actividad, id=actividad_id)

    if request.method == 'POST':
        seccion.delete()
        return redirect('ver_secciones', resultado_id=resultado_id, actividad_id=actividad_id)

    return render(request, 'main/secciones/eliminar_secciones.html', {'seccion': seccion, 'resultado': resultado, 'actividad_id': actividad_id})

@login_required(login_url='user_login')
def editar_secciones(request, resultado_id, actividad_id, id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    seccion = get_object_or_404(Seccion, id=id)

    if request.method == 'POST':
        seccion.nombre = request.POST.get('nombre')
        seccion.contenido = request.POST.get('contenido')
        seccion.avance = request.POST.get('avance')
        seccion.save()
        return redirect('ver_secciones', resultado_id=resultado_id, actividad_id=actividad_id)

    return render(request, 'main/secciones/editar_secciones.html', {'seccion': seccion, 'resultado': resultado, 'actividad_id': actividad_id})

@login_required(login_url='user_login')
def crear_secciones(request, resultado_id, actividad_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividad = get_object_or_404(Actividad, id=actividad_id)

    if request.method == 'POST':
        nombre = request.POST['nombre']
        avance = request.POST['avance']
        contenido = request.POST['contenido']

        seccion = actividad.seccion_set.create(
            nombre=nombre,
            avance=avance,
            contenido=contenido
            )
        seccion.save()
        return redirect('ver_secciones', resultado_id=resultado_id, actividad_id=actividad_id)

    return render(request, 'main/secciones/crear_secciones.html', {'actividad': actividad, 'resultado': resultado, 'actividad_id': actividad_id})

@login_required(login_url='user_login')
def eliminra_actividad(request, resultado_id, actividad_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividad = get_object_or_404(Actividad, id=actividad_id)
    if request.method == 'POST':
        actividad.delete()
        return redirect('ver_actividad', resultado_id=resultado.id)
    return render(request, 'main/actividad/eliminar_actividad.html', {'actividad': actividad, 'resultado': resultado,})

@login_required(login_url='user_login')
def editar_actividad(request, resultado_id, actividad_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividad = get_object_or_404(Actividad, id=actividad_id)

    if request.method == 'POST':
        actividad.nombre = request.POST.get('nombre')
        actividad.contenido = request.POST.get('contenido')
        actividad.fecha = request.POST.get('fecha')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        actividad.fecha_vencimiento = timezone.make_aware(datetime.strptime(fecha_vencimiento, '%Y-%m-%dT%H:%M'))
        actividad.save()
        
        return redirect('ver_actividad', resultado_id=resultado.id)
    
    return render(request, 'main/actividad/editar_actividad.html', {'actividad': actividad})

@login_required(login_url='user_login')
def crear_actividad(request, resultado_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)

    if request.method == 'POST':
        nombre = request.POST['nombre']
        contenido = request.POST['contenido']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        fecha = request.POST['fecha']

        actividad = resultado.actividad_set.create(
            nombre=nombre,
            contenido=contenido,
            fecha=fecha,
            fecha_vencimiento=fecha_vencimiento,
            fecha_actual=timezone.now()
        )
        actividad.save()
        return redirect('ver_actividad', resultado_id=resultado.id)
    
    return render(request, 'main/actividad/crear_actividad.html', {'resultado': resultado})

@login_required(login_url='user_login')
def ver_actividad(request, resultado_id):
    resultado = get_object_or_404(Resultado, id=resultado_id)
    actividades = resultado.actividad_set.all()

    return render(request, 'main/actividad/ver_actividad.html', {'resultado': resultado, 'actividades': actividades,})

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
    

