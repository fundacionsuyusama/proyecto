from django.db import models
from django.utils import timezone

class Resultado(models.Model):
    nombre = models.CharField(max_length=255)
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now, editable=False)
    promedio_avance = models.FloatField(default=0)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    contenido = models.TextField()
    is_completed = models.BooleanField(default=False)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    fecha_actual = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nombre

class Seccion(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    contenido = models.TextField()
    avance = models.IntegerField(default=False)
    fecha_vencimiento_seccion = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Avance(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    contenido = models.IntegerField()

    def __str__(self):
        return self.contenido
    
class Dificultad(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    contenido = models.TextField()

    def __str__(self):
        return self.contenido

class Alternativa(models.Model):
    dificultad = models.ForeignKey(Dificultad, on_delete=models.CASCADE)
    contenido = models.TextField()

    def __str__(self):
        return self.contenido
    

    
class Cumplido(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    cumplida = models.TextField(blank=True)
    
    def __str__(self):
        return self.cumplida
    
class Proceso(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    proceso = models.TextField(blank=True)

    def __str__(self):
        return self.proceso
    
class Urgente(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    urgente = models.TextField(blank=True)

    def __str__(self):
        return self.urgente
    