from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from products.models import Producto


class CarritoTests(TestCase):

    def setUp(self):
        vendedor = CustomUser.objects.create_user(username='ven', password='Clave12345!', role='VENDEDOR')
        self.producto = Producto.objects.create(
            vendedor=vendedor, nombre='Llave Allen', precio=50000, existencias=3
        )
        self.url_agregar = reverse('cart_add', args=[self.producto.id])
        self.url_quitar = reverse('cart_remove', args=[self.producto.id])
        self.id = str(self.producto.id)

    def test_agregar_producto(self):
        self.client.post(self.url_agregar, {'quantity': 2})
        self.assertEqual(self.client.session['cart'][self.id]['quantity'], 2)

    def test_no_supera_existencias(self):
        self.client.post(self.url_agregar, {'quantity': 10})
        self.assertEqual(self.client.session['cart'][self.id]['quantity'], 3)

    def test_quitar_producto(self):
        self.client.post(self.url_agregar, {'quantity': 1})
        self.client.post(self.url_quitar)
        self.assertNotIn(self.id, self.client.session['cart'])

    def test_agregar_por_get_no_esta_permitido(self):
        respuesta = self.client.get(self.url_agregar)
        self.assertEqual(respuesta.status_code, 405)