from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar-clientes'),
    path('criar/', views.criar_cliente, name='criar-cliente'),
    path('<int:id>/', views.detalhes_cliente, name='detalhes-cliente'),
]