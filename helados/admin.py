from django.contrib import admin
from helados.models import Helados

# Register your models here.
class HeladosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    list_filter = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Helados, HeladosAdmin)