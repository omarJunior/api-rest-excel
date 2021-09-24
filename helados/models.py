from django.db import models

# Create your models here.
class Helados(models.Model):
	nombre = models.CharField(max_length = 85)
	precio = models.CharField(max_length = 90)
	stock = models.CharField(max_length= 60)

	class Meta:
		db_table = 'helados'
