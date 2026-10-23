from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from products.models import Producto
from .cart import Cart
from .models import Order, OrderItem


# ---------- CARRITO ----------

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'orders/cart.html', {'cart': cart})


@require_POST
def cart_add(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)

    try:
        cantidad = int(request.POST.get('quantity', 1))
    except ValueError:
        cantidad = 1
    cantidad = max(1, cantidad)

    # No permitir más unidades de las que hay en existencias
    ya_en_carrito = cart.cart.get(str(producto.id), {}).get('quantity', 0)
    cantidad = min(cantidad, producto.existencias - ya_en_carrito)

    if cantidad > 0:
        cart.add(producto, cantidad)
    return redirect('cart_detail')


@require_POST
def cart_remove(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    cart.remove(producto)
    return redirect('cart_detail')


# ---------- PEDIDOS (para la presentación final, todavía sin URL) ----------

@login_required
def order_history(request):
    orders = request.user.orders.all()
    return render(request, 'orders/order_history.html', {'orders': orders})


def order_create(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('cart_detail')

    if request.method == 'POST':
        # transaction.atomic: si algo falla a mitad de camino, se deshace TODO
        with transaction.atomic():
            order = Order.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                address=request.POST.get('address'),
                postal_code=request.POST.get('postal_code', ''),
                city=request.POST.get('city'),
                user=request.user if request.user.is_authenticated else None,
            )
            for item in cart:
                producto = item['product']
                quantity = item['quantity']
                OrderItem.objects.create(
                    order=order, product=producto, price=item['price'], quantity=quantity
                )
                producto.existencias = max(0, producto.existencias - quantity)
                producto.save()
        cart.clear()
        return render(request, 'orders/order_created.html', {'order': order})

    return render(request, 'orders/order_create.html', {'cart': cart})