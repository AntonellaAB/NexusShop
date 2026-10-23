from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from products.models import Categoria, Producto


class CatalogoTests(TestCase):

    def setUp(self):
        vendedor = CustomUser.objects.create_user(username='ven', password='Clave12345!', role='VENDEDOR')
        self.herramientas = Categoria.objects.create(nombre='Herramientas')
        self.pinturas = Categoria.objects.create(nombre='Pinturas')
        self.llave = Producto.objects.create(
            vendedor=vendedor, nombre='Llave Allen', precio=50000,
            existencias=5, categoria=self.herramientas,
        )
        self.latex = Producto.objects.create(
            vendedor=vendedor, nombre='Pintura látex', precio=120000,
            existencias=0, categoria=self.pinturas,
        )

    def test_catalogo_es_publico_y_muestra_productos(self):
        respuesta = self.client.get(reverse('catalogo'))
        self.assertContains(respuesta, 'Llave Allen')
        self.assertContains(respuesta, 'Pintura látex')

    def test_filtro_por_categoria(self):
        respuesta = self.client.get(reverse('catalogo'), {'categoria': self.herramientas.id})
        self.assertContains(respuesta, 'Llave Allen')
        self.assertNotContains(respuesta, 'Pintura látex')

    def test_busqueda_por_nombre(self):
        respuesta = self.client.get(reverse('catalogo'), {'q': 'llave'})
        self.assertContains(respuesta, 'Llave Allen')
        self.assertNotContains(respuesta, 'Pintura látex')

    def test_categoria_invalida_no_rompe(self):
        respuesta = self.client.get(reverse('catalogo'), {'categoria': 'abc'})
        self.assertEqual(respuesta.status_code, 200)

    def test_detalle_de_producto(self):
        respuesta = self.client.get(reverse('producto_detalle', args=[self.llave.id]))
        self.assertContains(respuesta, 'Llave Allen')
        self.assertContains(respuesta, '5 disponibles')

    def test_detalle_sin_stock(self):
        respuesta = self.client.get(reverse('producto_detalle', args=[self.latex.id]))
        self.assertContains(respuesta, 'Sin stock')

    def test_producto_inexistente_da_404(self):
        respuesta = self.client.get(reverse('producto_detalle', args=[9999]))
        self.assertEqual(respuesta.status_code, 404)

    def test_carrito_muestra_producto_agregado(self):
        self.client.post(reverse('cart_add', args=[self.llave.id]), {'quantity': 2})
        respuesta = self.client.get(reverse('cart_detail'))
        self.assertContains(respuesta, 'Llave Allen')