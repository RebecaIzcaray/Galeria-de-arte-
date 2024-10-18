from django import forms
from .models import Obra

class ObraForma(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['titulo', 'genero', 'dimensiones', 'año', 'precio', 'nombre_artista', 'nacionalidad']