from django.db import models

class Mecanico(models.Model):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=100)
    equipe = models.ForeignKey('Equipe', on_delete=models.SET_NULL, null=True)

class Equipe(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome