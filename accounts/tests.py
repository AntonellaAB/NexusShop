from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.http import HttpResponse
from .models import CustomUser
from .decorators import vendedor_required

CLAVE = 'ClaveSegura123!'


class RegistroTests(TestCase):

    def datos_registro(self, **cambios):
        datos = {
            'username': 'juanperez',
            'email': 'juan@test.com',
            'first_name': 'Juan',
            'last_name': 'Pérez',
            'phone': '0981000000',
            'address': 'Asunción',
            'password1': CLAVE,
            'password2': CLAVE,
        }
        datos.update(cambios)
        return datos

    def test_registro_crea_cliente_y_lo_loguea(self):
        respuesta = self.client.post(reverse('registro'), self.datos_registro())
        self.assertRedirects(respuesta, reverse('home'))
        usuario = CustomUser.objects.get(username='juanperez')
        self.assertEqual(usuario.role, 'CLIENTE')
        self.assertIn('_auth_user_id', self.client.session)  # quedó logueado

    def test_registro_con_claves_distintas_falla(self):
        respuesta = self.client.post(
            reverse('registro'), self.datos_registro(password2='OtraClave999!')
        )
        self.assertEqual(respuesta.status_code, 200)  # vuelve a mostrar el form
        self.assertFalse(CustomUser.objects.filter(username='juanperez').exists())


class LoginLogoutTests(TestCase):

    def setUp(self):
        # setUp se ejecuta antes de CADA test
        self.usuario = CustomUser.objects.create_user(username='maria', password=CLAVE)

    def test_login_correcto(self):
        respuesta = self.client.post(reverse('login'), {'username': 'maria', 'password': CLAVE})
        self.assertRedirects(respuesta, reverse('home'))
        self.assertIn('_auth_user_id', self.client.session)

    def test_login_con_clave_incorrecta(self):
        respuesta = self.client.post(reverse('login'), {'username': 'maria', 'password': 'mal'})
        self.assertEqual(respuesta.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_logout_por_post(self):
        self.client.login(username='maria', password=CLAVE)
        self.client.post(reverse('logout'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_logout_por_get_no_esta_permitido(self):
        respuesta = self.client.get(reverse('logout'))
        self.assertEqual(respuesta.status_code, 405)


class RolesTests(TestCase):

    def setUp(self):
        self.cliente = CustomUser.objects.create_user(username='cli', password=CLAVE, role='CLIENTE')
        self.vendedor = CustomUser.objects.create_user(username='ven', password=CLAVE, role='VENDEDOR')
        self.factory = RequestFactory()

        @vendedor_required
        def vista_de_prueba(request):
            return HttpResponse('ok')
        self.vista = vista_de_prueba

    def test_propiedades_de_rol(self):
        self.assertTrue(self.vendedor.es_vendedor)
        self.assertFalse(self.cliente.es_vendedor)
        self.assertTrue(self.cliente.es_cliente)

    def test_cliente_no_puede_entrar_a_vista_de_vendedor(self):
        request = self.factory.get('/prueba/')
        request.user = self.cliente
        respuesta = self.vista(request)
        self.assertEqual(respuesta.status_code, 302)  # lo redirige al login

    def test_vendedor_si_puede_entrar(self):
        request = self.factory.get('/prueba/')
        request.user = self.vendedor
        respuesta = self.vista(request)
        self.assertEqual(respuesta.status_code, 200)