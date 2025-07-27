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


class Contrato(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, verbose_name='Imóvel')
    locatario = models.ForeignKey(Locatario, on_delete=models.CASCADE, verbose_name='Locatário')
    valor_aluguel = models.DecimalField('Valor aluguel', max_digits=10, decimal_places=2)
    valor_iptu = models.DecimalField('Valor IPTU',     max_digits=10, decimal_places=2)
    iptu_parcelas = models.PositiveSmallIntegerField('IPTU parcelas', default=10)
    data_inicio = models.DateField('Início do contrato')
    data_fim    = models.DateField('Término do contrato', null=True, blank=True)

    def __str__(self):
        return f'{self.locatario} → {self.imovel}'


class Taxa(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='taxas')
    nome     = models.CharField('Nome da taxa', max_length=100)
    valor    = models.DecimalField('Valor da taxa', max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.nome}: {self.valor}'



