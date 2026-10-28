from django.shortcuts import render, redirect
from clientes.models import Cliente
from produtos.models import Produto
from .models import Pedido, ItemPedido
from django.contrib import messages

def lista_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-id')
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

def registro_pedido(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = int(request.POST.get('quantidade'))
        
        cliente = Cliente.objects.get(id=cliente_id)
        produto = Produto.objects.get(id=produto_id)
        
        # 1. Validação: Tem estoque suficiente?
        if produto.estoque < quantidade:
            messages.error(request, f'Estoque insuficiente! Disponível: {produto.estoque}')
            return redirect('registro_pedido')
        
        # 2. Cria o Pedido
        pedido = Pedido.objects.create(cliente=cliente)
        
        # 3. Cria o Item do Pedido
        item = ItemPedido.objects.create(
            pedido=pedido,
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco
        )
        
        # 4. Atualiza o total do Pedido
        pedido.total = item.subtotal
        pedido.save()
        
        # 5. DÁ BAIXA NO ESTOQUE DO PRODUTO
        produto.estoque -= quantidade
        produto.save()
        
        messages.success(request, 'Pedido registrado e estoque atualizado!')
        return redirect('lista_pedidos')
        
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'pedidos/registro_pedidos.html', {
        'clientes': clientes,
        'produtos': produtos
    })