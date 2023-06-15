from django.db import models
from django.utils import timezone

class Resultado(models.Model):
    nombre = models.CharField(max_length=255)
    texto = models.CharField(max_length=300)
    fecha = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    contenido = models.CharField(max_length=400)
    is_completed = models.BooleanField(default=False)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    fecha_actual = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nombre

class Seccion(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre