from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Cliente
import json

def listar_clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        data = [{
            'id': c.id,
            'nome': c.nome,
            'telefone': c.telefone,
            'endereco': c.endereco
        } for c in clientes]
        return JsonResponse(data, safe=False)

@csrf_exempt
def criar_cliente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.create(
                nome=data['nome'],
                telefone=data.get('telefone', ''),
                endereco=data.get('endereco', '')
            )
            return JsonResponse({'id': cliente.id, 'message': 'Cliente criado com sucesso!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def detalhes_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'GET':
        return JsonResponse({'id': cliente.id, 'nome': cliente.nome, 'telefone': cliente.telefone, 'endereco': cliente.endereco})
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        cliente.nome = data.get('nome', cliente.nome)
        cliente.telefone = data.get('telefone', cliente.telefone)
        cliente.endereco = data.get('endereco', cliente.endereco)
        cliente.save()
        return JsonResponse({'message': 'Cliente atualizado!'})
        
    elif request.method == 'DELETE':
        cliente.delete()
        return JsonResponse({'message': 'Cliente excluído!'})
        
    return JsonResponse({'error': 'Método não permitido'}, status=405)