from django.contrib import admin
from .models import Proprietario, Imovel, Locatario, Contrato, Taxa

# Inline de Imóvel dentro de Proprietário
class ImovelInline(admin.TabularInline):
    model = Imovel
    extra = 1

@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    inlines = [ImovelInline]

# Inline de Contrato dentro de Imóvel
class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 1

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ['endereco', 'proprietario']
    inlines = [ContratoInline]

# Inline de Taxa dentro de Contrato
class TaxaInline(admin.TabularInline):
    model = Taxa
    extra = 1

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ['imovel', 'locatario', 'valor_aluguel', 'valor_iptu']
    inlines = [TaxaInline]

# Registrar Locatários e Taxas diretamente
@admin.register(Locatario)
class LocatarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']

@admin.register(Taxa)
class TaxaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor', 'contrato']

