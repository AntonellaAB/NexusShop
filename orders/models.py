
from django.db import models
from products.models import Product
from django.conf import settings

class Order(models.Model):
    # Relación opcional con el usuario registrado (historial del cliente)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')
    
    # Datos de contacto y envío del cliente
    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Correo Electrónico")
    address = models.CharField(max_length=250, verbose_name="Dirección")
    postal_code = models.CharField(max_length=20, verbose_name="Código Postal")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    
    # Metadatos del pedido
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    paid = models.BooleanField(default=False, verbose_name="Pagado")

    class Meta:
        ordering = ['-created']
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f'Pedido #{self.id}'

    def get_total_cost(self):
        #Calcula el costo total sumando todos los artículos del pedido.
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    # Relación con el pedido principal
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    
    # Relación con el producto comprado
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    
    # Precio e historial de la cantidad al momento de la compra
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio unitario")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        #Calcula el subtotal de este artículo específico.
        return self.price * self.quantity