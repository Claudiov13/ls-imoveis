from django.contrib import admin
from .models import Proprietario, Locatario, Imovel

admin.site.register(Proprietario)
admin.site.register(Locatario)
admin.site.register(Imovel)

