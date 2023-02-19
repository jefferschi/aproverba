#from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Verba, PedidoCompra

# para requerer login ao acessar as páginas, mesmo digitando o endereço no navegador
from django.contrib.auth.mixins import LoginRequiredMixin

# redireciona o usuário depois de fazer algo
from django.urls import reverse_lazy

# para gerenciar permissões por grupos. Pode ser feito pelo gerenciador do djaango, mas aqui será pelo braces
from braces.views import GroupRequiredMixin


""" classes ListView - para listar os registros pelo formulário"""
class VerbaList(GroupRequiredMixin, LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    group_required = u'Aprovador'
    model = Verba
    template_name = 'fluxo/listas/lista-verbas.html'