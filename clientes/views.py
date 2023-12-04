from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Carro
import re 
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

def clientes(request):
    if request.method == "GET":
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes' : clientes_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        marcas = request.POST.getlist('marca')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf)
        
        if cliente.exists():
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome':sobrenome, 'email': email, 'carros': zip(carros, marcas, placas, anos)})
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome':sobrenome, 'cpf':cpf, 'carros': zip(carros, marcas, placas, anos)})
            
        cliente = Cliente(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf
        )
        
        cliente.save()
        
        for carro, marca, placa, ano in zip(carros, marcas, placas, anos):  # Adiciona a marca à lista de parâmetros
            car = Carro(
                carro=carro,
                marca=marca, 
                placa=placa,
                ano=ano,
                cliente=cliente
            )
            car.save()
            
        return HttpResponse('Cliente registrado com sucesso')
    
def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    carros = Carro.objects.filter(cliente=cliente[0])
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']
    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [{'fields': carro['fields'], 'id': carro['pk']} for carro in carros_json]
    data = {'cliente': cliente_json, 'carros': carros_json, 'cliente_id': cliente_id}
    return JsonResponse(data)

@csrf_exempt
def update_carro(request, id):
    nome_carro = request.POST.get('carro')
    placa = request.POST.get('placa')
    ano = request.POST.get('ano')

    carro = Carro.objects.get(id=id)
    list_carros = Carro.objects.exclude(id=id).filter(placa=placa)

    if list_carros.exists():
        return HttpResponse('Placa já existente') 
        
    carro.carro = nome_carro
    carro.placa = placa
    carro.ano = ano
    carro.save()

    return HttpResponse("dados alterados com sucesso")

def excluir_carro(request, id):
    try: 
        carro = Carro.objects.get(id=id)
        cliente_id = carro.cliente.id
        carro.delete()
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={cliente_id}')
    except:
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={cliente_id}')

def update_cliente(request, id):
    body = json.loads(request.body)
    
    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']
    
    try:
        cliente = get_object_or_404(Cliente, id=id)
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.save()
        return JsonResponse({'status' : '200', 'nome' : nome, 'sobrenome' : sobrenome, 'email' : email, 'cpf' : cpf})
    except:
        return JsonResponse({'status' : '500'})
    
def add_carro(request):
    if request.method == 'POST':
        carro = request.POST.get('carro')
        marca = request.POST.get('marca')
        placa = request.POST.get('placa')
        ano = request.POST.get('ano')
        cliente_id = request.POST.get('cliente_id')

        cliente = get_object_or_404(Cliente, pk=cliente_id)

        novo_carro = Carro(carro=carro, marca=marca, placa=placa, ano=ano, cliente=cliente)
        novo_carro.save()

        messages.success(request, 'Carro adicionado com sucesso')
        return redirect('clientes')  
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)