# reservas/forms.py
from django import forms
from .models import Campista, Reserva

class CampistaForm(forms.ModelForm):
    class Meta:
        model = Campista
        fields = ['nombre', 'correo', 'telefono', 'direccion']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['campista', 'fecha_inicio', 'fecha_fin', 'tipo_alojamiento', 'numero_personas', 'estado', 'observaciones']
