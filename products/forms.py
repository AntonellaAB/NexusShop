from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'descripcion', 'precio', 'existencias', 'imagen']


class StockForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['existencias']