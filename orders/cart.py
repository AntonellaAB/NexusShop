from decimal import Decimal
from products.models import Producto


class Cart:
    def __init__(self, request):
        # Inicializa el carrito usando la sesión del usuario.
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, producto, quantity=1, override_quantity=False):
        # Añade un producto al carrito o actualiza su cantidad.
        producto_id = str(producto.id)
        if producto_id not in self.cart:
            self.cart[producto_id] = {
                'quantity': 0,
                'price': str(producto.precio),  # string para que se pueda guardar en la sesión (JSON)
            }
        if override_quantity:
            self.cart[producto_id]['quantity'] = quantity
        else:
            self.cart[producto_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Marca la sesión como modificada para que Django la guarde.
        self.session.modified = True

    def remove(self, producto):
        # Elimina un producto del carrito.
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def __iter__(self):
        # Devuelve los ítems del carrito con su producto de la base de datos.
        # Arma diccionarios NUEVOS en lugar de modificar los de la sesión,
        # así nunca se guarda un objeto Producto dentro de la sesión.
        productos = Producto.objects.filter(id__in=self.cart.keys())
        for producto in productos:
            item = self.cart[str(producto.id)]
            precio = Decimal(item['price'])
            yield {
                'product': producto,
                'quantity': item['quantity'],
                'price': precio,
                'total_price': precio * item['quantity'],
            }

    def __len__(self):
        # Cantidad total de unidades en el carrito.
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        # Precio total del carrito.
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # Vacía el carrito (después de pagar).
        del self.session['cart']
        self.save()