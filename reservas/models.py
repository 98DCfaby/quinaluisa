from django.db import models

# Create your models here.
class Campista(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    TIPO_ALOJAMIENTO = [
        ('Tienda', 'Tienda'),
        ('Cabaña', 'Cabaña'),
        ('Caravana', 'Caravana'),
    ]
    ESTADO_RESERVA = [
        ('Confirmada', 'Confirmada'),
        ('Pendiente', 'Pendiente'),
        ('Cancelada', 'Cancelada'),
    ]

    campista = models.ForeignKey(Campista, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo_alojamiento = models.CharField(max_length=20, choices=TIPO_ALOJAMIENTO)
    numero_personas = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_RESERVA)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Reserva de {self.campista.nombre} ({self.estado})'