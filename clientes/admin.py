from django.contrib import admin
from clientes.models import Clientes

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombres','apellidos','correo','direccion','telefono', 'empresa')
    list_filter=('apellidos',)
    search_fields=('nombre',)
admin.site.register(Clientes, ClienteAdmin)  