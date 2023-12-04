from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField(default='')

    def __str__(self):
        return self.nome