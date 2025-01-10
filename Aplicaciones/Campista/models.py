from django.db import models

# Create your models here.
class Campista(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    direccion = models.TextField()