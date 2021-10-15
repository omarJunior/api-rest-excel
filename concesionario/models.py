from django.db import models

# Create your models here.
class Concesionario(models.Model):
    codigo = models.CharField(max_length=80)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=70)
    ciudad = models.CharField(max_length=80)
    tipo = models.CharField(max_length=50)
    cantidad_vehiculos = models.IntegerField()
    descripcion = models.TextField()
    renta = models.CharField(max_length=80)
    cordinador = models.CharField(max_length=90)

    class Meta:
        db_table = 'concesionario'