from django.contrib import admin
from vehiculos.models import Vehiculos

# Register your models here.
class VehiculosAdmin(admin.ModelAdmin):
    list_display =('placa', 'modelo', 'marca', 'color', 'precio', 'descripcion')
    list_filter = ('marca', 'color',)
    search_fields = ('placa', 'marca', 'color',)

admin.site.register(Vehiculos, VehiculosAdmin)
