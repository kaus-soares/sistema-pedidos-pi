from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('registrar/', views.registro_pedido, name='registro_pedido'),
]