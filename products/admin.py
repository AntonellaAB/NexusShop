from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'vendedor', 'categoria', 'precio', 'existencias')
    list_filter = ('categoria', 'vendedor')
    search_fields = ('nombre', 'descripcion')