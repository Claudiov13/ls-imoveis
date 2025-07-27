from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Proprietario, Locatario, Imovel

# ——— Home protegido ———
@login_required(login_url='login')
def home(request):
    return render(request, 'core/home.html')

# ——— CRUD de Proprietário ———
class ProprietarioList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Proprietario
    template_name = 'core/proprietario_list.html'
    context_object_name = 'props'

class ProprietarioCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Proprietario
    fields = ['nome', 'documento']
    template_name = 'core/proprietario_form.html'
    success_url = reverse_lazy('core:prop_list')

class ProprietarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Proprietario
    fields = ['nome', 'documento']
    template_name = 'core/proprietario_form.html'
    success_url = reverse_lazy('core:prop_list')

class ProprietarioDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Proprietario
    template_name = 'core/proprietario_confirm_delete.html'
    success_url = reverse_lazy('core:prop_list')


# ——— CRUD de Locatário ———
class LocatarioList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Locatario
    template_name = 'core/locatario_list.html'
    context_object_name = 'locs'

class LocatarioCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Locatario
    fields = ['nome', 'email', 'telefone']
    template_name = 'core/locatario_form.html'
    success_url = reverse_lazy('core:loc_list')

class LocatarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Locatario
    fields = ['nome', 'email', 'telefone']
    template_name = 'core/locatario_form.html'
    success_url = reverse_lazy('core:loc_list')

class LocatarioDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Locatario
    template_name = 'core/locatario_confirm_delete.html'
    success_url = reverse_lazy('core:loc_list')


# ——— CRUD de Imóvel ———
class ImovelList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Imovel
    template_name = 'core/imovel_list.html'
    context_object_name = 'imoveis'

class ImovelCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Imovel
    fields = ['endereco', 'proprietario']
    template_name = 'core/imovel_form.html'
    success_url = reverse_lazy('core:imv_list')

class ImovelUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Imovel
    fields = ['endereco', 'proprietario']
    template_name = 'core/imovel_form.html'
    success_url = reverse_lazy('core:imv_list')

class ImovelDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Imovel
    template_name = 'core/imovel_confirm_delete.html'
    success_url = reverse_lazy('core:imv_list')
