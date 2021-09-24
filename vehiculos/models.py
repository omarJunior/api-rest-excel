from django.db import models

# Create your models here.
class Vehiculos(models.Model):
	placa = models.CharField(max_length = 50)
	modelo = models.CharField(max_length = 70)
	marca = models.CharField(max_length = 80)
	color = models.CharField(max_length = 80)
	precio = models.CharField(max_length = 70)
	descripcion = models.TextField()

	class Meta:
		db_table = 'vehiculos'