from django.conf import settings
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True, verbose_name='Imagen')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'VENDEDOR'},
        related_name='productos',
        verbose_name='Vendedor',
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='productos',
        verbose_name='Categoría',
    )
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    precio = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Precio (₲)')
    existencias = models.PositiveIntegerField(default=0, verbose_name='Existencias')
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name='Imagen')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre