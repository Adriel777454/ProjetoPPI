from django.db import models

class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.DecimalField(
        verbose_name=("valor"),
        decimal_places=2,
        max_digits=6
    )
    def __str__(self):
        return self.localizacao

class Reserva(models.Model):
    cnpj = models.CharField(max_length=20)
    nome_empresa = models.CharField(max_length=200)
    quitado = models.BooleanField(default=False)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_empresa

# Create your models here.
