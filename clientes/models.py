from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    cpf = models.CharField(max_length=12)
    
    def __str__(self):
        return self.nome
    
class Carro(models.Model):
    carro = models.CharField(max_length=100)
    marca = models.CharField(max_length=100) 
    placa = models.CharField(max_length=8)
    ano = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    consertos = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.carro