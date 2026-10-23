from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Categoria, Producto

# Create your tests here.

Usuario = get_user_model()
CLAVE = 'Clave12345x'


class PanelVendedorTests(TestCase):
    def setUp(self):
        self.vendedor = Usuario.objects.create_user(
            username='vendedor1', password=CLAVE, role='VENDEDOR')
        self.otro_vendedor = Usuario.objects.create_user(
            username='vendedor2', password=CLAVE, role='VENDEDOR')
        self.cliente = Usuario.objects.create_user(
            username='cliente1', password=CLAVE, role='CLIENTE')

        self.categoria = Categoria.objects.create(nombre='Tecnología')
        self.mi_producto = Producto.objects.create(
            vendedor=self.vendedor, categoria=self.categoria,
            nombre='Mi teclado', precio=150000, existencias=5)
        self.producto_ajeno = Producto.objects.create(
            vendedor=self.otro_vendedor,
            nombre='Producto ajeno', precio=90000, existencias=2)

    def datos_producto(self, **cambios):
        datos = {
            'categoria': self.categoria.pk,
            'nombre': 'Mouse gamer',
            'descripcion': 'Con luces',
            'precio': 80000,
            'existencias': 10,
        }
        datos.update(cambios)
        return datos

    def test_anonimo_es_enviado_al_login(self):
        respuesta = self.client.get(reverse('mis_productos'))
        self.assertRedirects(respuesta, f"{reverse('login')}?next={reverse('mis_productos')}", fetch_redirect_response=False)

    def test_cliente_no_entra_al_panel(self):
        self.client.login(username='cliente1', password=CLAVE)
        respuesta = self.client.get(reverse('mis_productos'))
        self.assertRedirects(respuesta, f"{reverse('login')}?next={reverse('mis_productos')}", fetch_redirect_response=False)

    def test_vendedor_solo_ve_sus_productos(self):
        self.client.login(username='vendedor1', password=CLAVE)
        respuesta = self.client.get(reverse('mis_productos'))
        self.assertContains(respuesta, 'Mi teclado')
        self.assertNotContains(respuesta, 'Producto ajeno')

    def test_crear_producto_asigna_el_vendedor_logueado(self):
        self.client.login(username='vendedor1', password=CLAVE)
        respuesta = self.client.post(reverse('producto_crear'), self.datos_producto())
        self.assertRedirects(respuesta, reverse('mis_productos'))
        nuevo = Producto.objects.get(nombre='Mouse gamer')
        self.assertEqual(nuevo.vendedor, self.vendedor)

    def test_no_permite_existencias_negativas(self):
        self.client.login(username='vendedor1', password=CLAVE)
        respuesta = self.client.post(
            reverse('producto_crear'), self.datos_producto(existencias=-1))
        self.assertEqual(respuesta.status_code, 200)  # vuelve al formulario
        self.assertFalse(Producto.objects.filter(nombre='Mouse gamer').exists())

    def test_vendedor_no_puede_editar_producto_ajeno(self):
        self.client.login(username='vendedor1', password=CLAVE)
        url = reverse('producto_editar', args=[self.producto_ajeno.pk])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_vendedor_no_puede_eliminar_producto_ajeno(self):
        self.client.login(username='vendedor1', password=CLAVE)
        url = reverse('producto_eliminar', args=[self.producto_ajeno.pk])
        self.assertEqual(self.client.post(url).status_code, 404)
        self.assertTrue(Producto.objects.filter(pk=self.producto_ajeno.pk).exists())

    def test_vendedor_elimina_su_propio_producto(self):
        self.client.login(username='vendedor1', password=CLAVE)
        url = reverse('producto_eliminar', args=[self.mi_producto.pk])
        respuesta = self.client.post(url)
        self.assertRedirects(respuesta, reverse('mis_productos'))
        self.assertFalse(Producto.objects.filter(pk=self.mi_producto.pk).exists())