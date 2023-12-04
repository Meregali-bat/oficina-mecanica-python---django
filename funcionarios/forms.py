from django import forms
from .models import Mecanico, Equipe

class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = ['codigo', 'nome', 'endereco', 'especialidade', 'equipe']

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome']