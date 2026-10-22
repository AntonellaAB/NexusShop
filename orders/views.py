from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .cart import Cart

@login_required
def order_history(request):
    # Obtiene todos los pedidos del usuario autenticado ordenados del más reciente al más antiguo
    orders = request.user.orders.all()
    return render(request, 'orders/order_history.html', {'orders': orders})

def order_create(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        # 1. Crear el pedido principal con los datos enviados por el formulario
        order = Order.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            postal_code=request.POST.get('postal_code'),
            city=request.POST.get('city'),
            user=request.user if request.user.is_authenticated else None
        )
        
        # 2. Recorrer los elementos que están en el carrito de la sesión
        for item in cart:
            producto = item['product']
            quantity = item['quantity']
            price = item['price']
            
            # Crear el registro de cada artículo en el pedido
            OrderItem.objects.create(
                order=order,
                product=producto,
                price=price,
                quantity=quantity
            )
            
            # 3. Reducir el inventario del producto en la base de datos usando 'existencias'
            producto.existencias -= quantity
            producto.save()
            
        # 4. Vaciar el carrito de la sesión para que quede limpio
        cart.clear()
        
        # 5. Redirigir a una pantalla de confirmación o éxito
        return render(request, 'orders/order_created.html', {'order': order})
        
    return render(request, 'orders/order_create.html', {'cart': cart})