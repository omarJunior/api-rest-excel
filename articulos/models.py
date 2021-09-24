from django.db import models

# Create your models here.
class Articulos(models.Model):
    nombres = models.CharField(max_length=90)
    precio = models.CharField(max_length=85)
    iva = models.CharField(max_length=90)
    descripcion = models.TextField()
    stock = models.IntegerField()
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=70)

    class Meta:
        db_table = 'articulos'
    
