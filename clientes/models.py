from django.db import models

# Create your models here.
class Clientes(models.Model):
	nombres = models.CharField(max_length = 80)
	apellidos = models.CharField(max_length = 80)
	direccion = models.CharField(max_length = 70)
	telefono = models.CharField(max_length = 80)
	correo = models.CharField(max_length = 100)
	ciudad = models.CharField(max_length = 80)
	empresa = models.CharField(max_length = 80)
	estatus = models.IntegerField()
	
	class Meta:
		db_table = 'clientes'