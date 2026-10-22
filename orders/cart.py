from decimal import Decimal
from products.models import Product  # Asegúrate de que coincida con tu app de productos

class Cart:
    def __init__(self, request):
        
        #Inicializa el carrito de compras utilizando la sesión del usuario.
        
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            # Si no hay un carrito en la sesión, creamos uno vacío
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        
        #Añade un producto al carrito o actualiza su cantidad.
        
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)  # Guardamos el precio como string por serialización JSON
            }
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
            
        self.save()

    def save(self):
        
        #Marca la sesión como 'modificada' para asegurarnos de que se guarde.
        
        self.session.modified = True

    def remove(self, product):
        
        #Elimina un producto del carrito.
        
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        
        #Itera sobre los elementos del carrito obteniendo los productos desde la base de datos.
        
        product_ids = self.cart.keys()
        # Traemos los objetos de la base de datos correspondientes a los IDs del carrito
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        
        #Calcula la cantidad total de artículos en el carrito.
        #
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        
        #Calcula el precio total a pagar por todos los productos del carrito.
        
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        
        #Vacía el carrito eliminándolo de la sesión (útil justo después de pagar).
        
        del self.session['cart']
        self.save()