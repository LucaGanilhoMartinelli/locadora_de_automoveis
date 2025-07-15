from django.db import models

class Automovel(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.TextField(blank=False, null=False)
    cor = models.CharField(max_length=50, blank=True, null=True)
    valor_diaria = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}'