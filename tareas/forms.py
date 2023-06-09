from django import forms
from .models import *

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['nombre','texto']