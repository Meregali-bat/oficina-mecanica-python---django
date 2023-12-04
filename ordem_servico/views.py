from django.shortcuts import render, redirect, get_object_or_404
from .models import OrdemServico, OrdemServicoPeca
from .forms import OrdemServicoForm, AdicionarPecaForm, AdicionarServicoForm
from django.http import HttpResponseRedirect
from datetime import datetime

def lista_ordens(request):
    ordens_concluidas = OrdemServico.objects.filter(concluida=True)
    ordens_nao_concluidas = OrdemServico.objects.filter(concluida=False)
    return render(request, 'lista_ordens.html', {'ordens_concluidas': ordens_concluidas, 'ordens_nao_concluidas': ordens_nao_concluidas})

def criar_ordem(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            ordem = form.save(commit=False)
            ordem.save()  
            form.save_m2m() 
            ordem.calcular_valor_total_pecas()  
            ordem.save()  
            return redirect('ordem_servico:lista_ordens')
    else:
        form = OrdemServicoForm()
    return render(request, 'criar_ordem.html', {'form': form})

def detalhes_ordem(request, id):
    ordem = get_object_or_404(OrdemServico, id=id)
    return render(request, 'detalhes_ordem.html', {'ordem': ordem})

def concluir_ordem(request, id):
    ordem = get_object_or_404(OrdemServico, id=id)
    if request.method == 'POST':
        form_peca = AdicionarPecaForm(request.POST, prefix='peca')
        form_servico = AdicionarServicoForm(request.POST, prefix='servico')
        if form_peca.is_valid() and form_servico.is_valid():
            peca = form_peca.cleaned_data['peca']
            quantidade = form_peca.cleaned_data['quantidade']
            servico = form_servico.cleaned_data['servico']
            OrdemServicoPeca.objects.create(ordem_servico=ordem, peca=peca, quantidade=quantidade)
            ordem.servicos.add(servico)
            ordem.calcular_valor_total_pecas()
            ordem.calcular_valor_total_servico()
            ordem.concluida = True
            ordem.data_conclusao = datetime.now()  # Define a data de conclusão como a data atual
            ordem.save()
            valor_total = ordem.calcular_valor_total()
            return redirect('ordem_servico:lista_ordens')
    else:
        form_peca = AdicionarPecaForm(prefix='peca')
        form_servico = AdicionarServicoForm(prefix='servico')
    return render(request, 'concluir_ordem.html', {'form_peca': form_peca, 'form_servico': form_servico, 'ordem': ordem})

def excluir_ordem(request, id):
    ordem = get_object_or_404(OrdemServico, id=id)
    if request.method == 'POST':
        ordem.delete()
        return HttpResponseRedirect('')  
    else:
        return render(request, 'excluir_ordem.html', {'ordem': ordem})