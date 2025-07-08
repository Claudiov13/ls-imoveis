from django.db import models

class Proprietario(models.Model):
    nome = models.CharField('Nome', max_length=200)
    documento = models.CharField('CPF/CNPJ', max_length=20)

    def __str__(self):
        return self.nome

class Locatario(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=20)

    def __str__(self):
        return self.nome

class Imovel(models.Model):
    endereco = models.CharField('Endereço', max_length=300)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.endereco

