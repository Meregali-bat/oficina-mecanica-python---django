from django import forms
from .models import Peca

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome', 'valor', 'quantidade_em_estoque']