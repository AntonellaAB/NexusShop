from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.cart_detail, name='cart_detail'),
    path('carrito/agregar/<int:producto_id>/', views.cart_add, name='cart_add'),
    path('carrito/quitar/<int:producto_id>/', views.cart_remove, name='cart_remove'),
]