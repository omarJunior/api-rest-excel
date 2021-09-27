from django.db import models

# Create your models here.
class SaberPro(models.Model):
    nombres = models.CharField(max_length=90)
    apellidos = models.CharField(max_length=90)
    genero = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=80)
    matematicas = models.IntegerField()
    lenguaje = models.IntegerField()
    ciencias = models.IntegerField()
    ingles = models.IntegerField()
    ciudadanas = models.IntegerField()
    fisica = models.IntegerField()

    class Meta:
        db_table = 'saberpros'