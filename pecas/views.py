from django.shortcuts import render, redirect
from .models import Peca
from .forms import PecaForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

def adicionar_peca(request):
    if request.method == "POST":
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pecas:listar_pecas')
    else:
        form = PecaForm()
    return render(request, 'adicionar_peca.html', {'form': form})

def remover_peca(request, peca_id):
    peca = get_object_or_404(Peca, id=peca_id)
    peca.delete()
    return redirect('pecas:listar_pecas')

def listar_pecas(request):
    pecas = Peca.objects.all()
    return render(request, 'pecas.html', {'pecas': pecas})