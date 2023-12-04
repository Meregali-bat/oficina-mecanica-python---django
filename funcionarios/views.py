from django.shortcuts import render, redirect, get_object_or_404
from .models import Mecanico, Equipe
from .forms import MecanicoForm, EquipeForm

def adicionar_mecanico(request):
    if request.method == "POST":
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios:listar_mecanicos')
    else:
        form = MecanicoForm()
    return render(request, 'adicionar_mecanico.html', {'form': form})

def remover_mecanico(request, mecanico_id):
    mecanico = get_object_or_404(Mecanico, id=mecanico_id)
    mecanico.delete()
    return redirect('funcionarios:listar_mecanicos')

def adicionar_mecanico_na_equipe(request, equipe_id, mecanico_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    mecanico = get_object_or_404(Mecanico, id=mecanico_id)
    mecanico.equipe = equipe
    mecanico.save()
    return redirect('funcionarios:detalhes_equipe', equipe_id=equipe.id)

def remover_mecanico_da_equipe(request, equipe_id, mecanico_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    mecanico = get_object_or_404(Mecanico, id=mecanico_id)
    if mecanico.equipe == equipe:
        mecanico.equipe = None
        mecanico.save()
    return redirect('funcionarios:detalhes_equipe', equipe_id=equipe.id)

def listar_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'listar_mecanicos.html', {'mecanicos': mecanicos})

def listar_equipes(request):
    equipes = Equipe.objects.all()
    return render(request, 'listar_equipes.html', {'equipes': equipes})

def adicionar_equipe(request):
    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios:listar_equipes')
    else:
        form = EquipeForm()
    return render(request, 'adicionar_equipe.html', {'form': form})

def detalhes_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    membros = Mecanico.objects.filter(equipe=equipe)
    return render(request, 'detalhes_equipe.html', {'equipe': equipe, 'membros': membros})

def editar_mecanico(request, mecanico_id):
    mecanico = get_object_or_404(Mecanico, id=mecanico_id)
    if request.method == "POST":
        form = MecanicoForm(request.POST, instance=mecanico)
        if form.is_valid():
            form.save()
            return redirect('funcionarios:listar_mecanicos')
    else:
        form = MecanicoForm(instance=mecanico)
    return render(request, 'editar_mecanico.html', {'form': form})

def remover_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    equipe.delete()
    return redirect('funcionarios:listar_equipes')