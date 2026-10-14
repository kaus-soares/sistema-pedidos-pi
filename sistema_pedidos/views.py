from django.shortcuts import render

def index (request):
    return render(request, 'index.html')

def clientes (request):
    return render(request, 'clientes.html')

def produtos (request):
    return render(request, 'produtos.html')