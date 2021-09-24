from django.db import models

# Create your models here.
class Productos(models.Model):
	codigo = models.CharField(max_length=40)
	productoName = models.CharField(max_length=80)
	precio = models.CharField(max_length=75)
	stock = models.CharField(max_length=40)
	unidad = models.IntegerField()
	descuento = models.CharField(max_length=30)
	total = models.CharField(max_length=70)

	class Meta:
	    db_table = 'productos'

