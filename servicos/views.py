from django.shortcuts import render, redirect, get_object_or_404
from .models import Servico
from .forms import ServicoForm

def criar_servico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicos:listar_servicos')
    else:
        form = ServicoForm()
    return render(request, 'servico_form.html', {'form': form})

def remover_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        servico.delete()
        return redirect('servicos:listar_servicos')
    return render(request, 'servico_confirm_delete.html', {'servico': servico})

def editar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servicos:listar_servicos')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'servico_form.html', {'form': form})

def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'listar_servicos.html', {'servicos': servicos})