from django.shortcuts import render, redirect, get_object_or_404

from accounts.decorators import vendedor_required
from .forms import ProductoForm
from .models import Producto

# Create your views here.

@vendedor_required
def mis_productos(request):
    productos = Producto.objects.filter(vendedor=request.user)
    return render(request, 'products/mis_productos.html', {'productos': productos})


@vendedor_required
def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user
            producto.save()
            return redirect('mis_productos')
    else:
        form = ProductoForm()
    return render(request, 'products/producto_form.html', {'form': form, 'titulo': 'Nuevo producto'})


@vendedor_required
def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk, vendedor=request.user)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('mis_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'products/producto_form.html', {'form': form, 'titulo': 'Editar producto'})


@vendedor_required
def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk, vendedor=request.user)
    if request.method == 'POST':
        producto.delete()
        return redirect('mis_productos')
    return render(request, 'products/producto_confirmar_eliminar.html', {'producto': producto})