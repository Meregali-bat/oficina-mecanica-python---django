from django.db import models

class Peca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_em_estoque = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - Valor: {self.valor} - Quantidade em estoque: {self.quantidade_em_estoque}"