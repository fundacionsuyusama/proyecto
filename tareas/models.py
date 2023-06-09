from django.db import models
from django.utils import timezone

class Resultado(models.Model):
    nombre = models.CharField(max_length=255)
    texto = models.CharField(max_length=300)
    fecha = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nombre