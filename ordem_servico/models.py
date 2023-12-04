from django.db import models
from pecas.models import Peca
from servicos.models import Servico
from clientes.models import Carro
from clientes.models import Cliente
from funcionarios.models import Equipe

class OrdemServicoPeca(models.Model):
    ordem_servico = models.ForeignKey('OrdemServico', on_delete=models.CASCADE)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=True)

class OrdemServico(models.Model):
    pecas = models.ManyToManyField(Peca, through=OrdemServicoPeca, blank=True)
    servicos = models.ManyToManyField(Servico, blank=True)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    valor_total_pecas = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, null=True, blank=True)
    valor_total_servico = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, null=True, blank=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True)
    problema_carro = models.TextField(null=True, blank=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    concluida = models.BooleanField(default=False)
    
    def calcular_valor_total_pecas(self):
        self.valor_total_pecas = sum(peca.valor * sum((osp.quantidade or 0) for osp in peca.ordemservicopeca_set.filter(ordem_servico=self)) for peca in set(self.pecas.all()))

    def calcular_valor_total_servico(self):
        self.valor_total_servico = sum(servico.valor for servico in self.servicos.all())

    def calcular_valor_total(self):
        self.calcular_valor_total_pecas()
        self.calcular_valor_total_servico()
        valor_total = self.valor_total_pecas + self.valor_total_servico
        return valor_total

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)