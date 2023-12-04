from django import forms
from .models import OrdemServico, Peca, Servico

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['cliente', 'carro', 'problema_carro']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()  # Salva a instância para que ela tenha um ID
        self.save_m2m()  # Salva as relações muitos-para-muitos
        return instance

class AdicionarPecaForm(forms.Form):
    peca = forms.ModelChoiceField(queryset=Peca.objects.all())
    quantidade = forms.IntegerField()

class AdicionarServicoForm(forms.Form):
    servico = forms.ModelChoiceField(queryset=Servico.objects.all())