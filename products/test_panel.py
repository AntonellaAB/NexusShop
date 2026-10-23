from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from products.models import Producto

CLAVE = 'Clave12345!'


class PanelVendedorTests(TestCase):

    def setUp(self):
        self.vendedor = CustomUser.objects.create_user(username='ven', password=CLAVE, role='VENDEDOR')
        otro = CustomUser.objects.create_user(username='otro', password=CLAVE, role='VENDEDOR')
        CustomUser.objects.create_user(username='cli', password=CLAVE, role='CLIENTE')
        self.mio = Producto.objects.create(vendedor=self.vendedor, nombre='Soldador', precio=200000, existencias=4)
        self.ajeno = Producto.objects.create(vendedor=otro, nombre='Taladro', precio=350000, existencias=2)

    def test_panel_muestra_solo_mis_productos(self):
        self.client.login(username='ven', password=CLAVE)
        respuesta = self.client.get(reverse('seller_dashboard'))
        self.assertContains(respuesta, 'Soldador')
        self.assertNotContains(respuesta, 'Taladro')

    def test_cliente_no_entra_al_panel(self):
        self.client.login(username='cli', password=CLAVE)
        respuesta = self.client.get(reverse('seller_dashboard'))
        self.assertEqual(respuesta.status_code, 302)

    def test_actualizar_stock(self):
        self.client.login(username='ven', password=CLAVE)
        self.client.post(reverse('producto_stock', args=[self.mio.pk]), {'existencias': 10})
        self.mio.refresh_from_db()
        self.assertEqual(self.mio.existencias, 10)

    def test_no_puede_cambiar_stock_de_otro_vendedor(self):
        self.client.login(username='ven', password=CLAVE)
        respuesta = self.client.post(reverse('producto_stock', args=[self.ajeno.pk]), {'existencias': 0})
        self.assertEqual(respuesta.status_code, 404)
        self.ajeno.refresh_from_db()
        self.assertEqual(self.ajeno.existencias, 2)