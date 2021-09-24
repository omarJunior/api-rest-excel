from django.db import models

# Create your models here.
class Calificaciones(models.Model):
	codinst = models.IntegerField()
	nombreinstitucion = models.CharField(max_length= 100)
	codigomunicipio = models.CharField(max_length = 80)
	nombremunicipio = models.CharField(max_length = 100)
	departamento = models.CharField(max_length = 80)
	calendario = models.CharField(max_length = 20)
	naturaleza = models.CharField(max_length = 50)
	jornada = models.CharField(max_length = 65)
	promediomatematica = models.CharField(max_length = 50)
	promedioquimica = models.CharField(max_length = 50)
	promediofisica = models.CharField(max_length = 50)
	promediobiologia = models.CharField(max_length = 50)
	promediofilosofia = models.CharField(max_length = 50)
	promedioingles = models.CharField(max_length = 50)
	promediolenguaje = models.CharField(max_length = 50)
	promediosociales = models.CharField(max_length = 50)
	desviacionmatematica = models.CharField(max_length = 50)
	desviacionquimica = models.CharField(max_length = 50)
	desviacionfisica = models.CharField(max_length = 50)
	desviacionbiologia = models.CharField(max_length = 50)
	desviacionfilosofia =models.CharField(max_length = 50)
	desviacioningles = models.CharField(max_length = 50)
	desviacionlenguaje = models.CharField(max_length = 50)
	desviacionsociales = models.CharField(max_length = 50)
	evaluados = models.CharField(max_length = 30)
	periodo = models.CharField(max_length = 50)

	class Meta:
		db_table = 'calificaciones'