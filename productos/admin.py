from django.contrib import admin
from productos.models import Productos

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'productoName', 'precio', 'stock', 'unidad', 'descuento', 'total')
    list_filter = ('productoName', 'precio',)
    search_fields = ('productoName',)

admin.site.register(Productos, ProductoAdmin)