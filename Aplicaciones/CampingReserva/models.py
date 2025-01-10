from django.db import models

# Create your models here.

from django.db import models
class Campista(models.Model):
    nombre_completo = models.CharField(max_length=255)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre_completo
class Reserva(models.Model):
    TIPOS_ALOJAMIENTO = [
        ('Tienda', 'Tienda'),
        ('Cabaña', 'Cabaña'),
        ('Caravana', 'Caravana'),
    ]
    ESTADOS_RESERVA = [
        ('Confirmada', 'Confirmada'),
        ('Pendiente', 'Pendiente'),
        ('Cancelada', 'Cancelada'),
    ]
    campista = models.ForeignKey(Campista, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo_alojamiento = models.CharField(max_length=10, choices=TIPOS_ALOJAMIENTO)
    numero_personas = models.PositiveIntegerField()
    estado_reserva = models.CharField(max_length=10, choices=ESTADOS_RESERVA)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reserva de {self.campista.nombre_completo}"