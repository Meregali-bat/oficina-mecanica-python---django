from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    valor = forms.DecimalField(label='Valor da Mão de Obra')
    class Meta:
        model = Servico
        fields = ['nome', 'valor']