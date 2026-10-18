from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar-produtos'),
    path('criar/', views.criar_produto, name='criar-produto'),
    path('<int:id>/', views.detalhes_produto, name='detalhes-produto'),
]