from django.contrib import admin
from concesionario.models import Concesionario

# Register your models here.
class ConcesionarioAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','direccion','ciudad','tipo','renta','cordinador')
    list_filter = ('nombre', 'ciudad',)
    search_fields = ('nombre',)
    
admin.site.register(Concesionario, ConcesionarioAdmin)

