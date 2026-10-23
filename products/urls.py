from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('mis-productos/', views.mis_productos, name='mis_productos'),
    path('nuevo/', views.producto_crear, name='producto_crear'),
    path('<int:pk>/editar/', views.producto_editar, name='producto_editar'),
    path('<int:pk>/eliminar/', views.producto_eliminar, name='producto_eliminar'),
]