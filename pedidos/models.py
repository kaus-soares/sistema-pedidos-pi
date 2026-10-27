from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from produtos.models import Produto
# Create your models here.
class Pedido(models.Model):

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-criado_em']
    
    def __str__(self):
        return self.nome


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens', verbose_name='Pedido')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, verbose_name='Produto')
    quantidade = models.IntegerField('Quantidade', default=1)
    preco_unitario = models.DecimalField('Preço Unitário', max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'
    
    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
    
    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)