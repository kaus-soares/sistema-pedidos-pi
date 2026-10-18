from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=20, decimal_places=2)
    estoque = models.IntegerField('Quantidade em Estoque', default=0)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"
