from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Produto
import json

def listar_produtos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        data = [{
            'id': p.id,
            'nome': p.nome,
            'preco': str(p.preco),
            'estoque': p.estoque,
        } for p in produtos]
        return JsonResponse(data, safe=False)

@csrf_exempt
def criar_produto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            produto = Produto.objects.create(
                nome=data['nome'],
                preco=data['preco'],
                estoque=data.get('estoque', 0)
            )
            return JsonResponse({'id': produto.id, 'message': 'Produto criado com sucesso!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def detalhes_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'GET':
        return JsonResponse({'id': produto.id, 'nome': produto.nome, 'preco': str(produto.preco), 'estoque': produto.estoque})
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        produto.nome = data.get('nome', produto.nome)
        produto.preco = data.get('preco', produto.preco)
        produto.estoque = data.get('estoque', produto.estoque)
        produto.save()
        return JsonResponse({'message': 'Produto atualizado!'})
        
    elif request.method == 'DELETE':
        produto.delete()
        return JsonResponse({'message': 'Produto excluído!'})
        
    return JsonResponse({'error': 'Método não permitido'}, status=405)