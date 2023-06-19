from django import forms
from .models import *

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['nombre','texto']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        nombre = nombre[0] + nombre[1:].lower()
        return nombre

    def clean_texto(self):
        texto = self.cleaned_data['texto']
        texto = texto[0] + texto[1:].lower()
        return texto