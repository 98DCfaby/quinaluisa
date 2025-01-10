

from django import forms
from .models import Campista, Reserva

class CampistaForm(forms.ModelForm):
    class Meta:
        model = Campista
        fields = '__all__'

from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['campista', 'fecha_inicio', 'fecha_fin', 'tipo_alojamiento', 'numero_personas', 'estado_reserva', 'observaciones']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tipo_alojamiento': forms.Select(attrs={'class': 'form-control'}),
            'numero_personas': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_reserva': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
        }
