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


######################################################################################
""" classes para Verba -  ListView, CreteView, UpdateView, DeleteView, """

# listar
class VerbaList(GroupRequiredMixin, LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    group_required = u'Aprovador'
    model = Verba
    template_name = 'fluxo/listas/lista-verbas.html'

# criar
class VerbaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'Aprovador'
    model = Verba
    fields = ['setor_verba','valor_verba','desc_verba','motivo_verba']
    template_name = 'fluxo/form-cad.html'
    success_url = reverse_lazy('lista-verbas')

# atualizar
class VerbaUpdate(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'Aprovador'
    model = Verba
    fields = ['setor_verba','valor_verba','desc_verba','motivo_verba']
    template_name = 'fluxo/form-cad.html'
    success_url = reverse_lazy('lista-verbas')

# apagar
class VerbaDelete(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'Aprovador'
    model = Verba
    template_name = 'fluxo/form-excl.html'
    success_url = reverse_lazy('lista-verbas')

######################################################################################
""" classes para Pedidos de Compra -  ListView, CreteView, UpdateView, DeleteView, """

# listar
class PCList(GroupRequiredMixin, LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    group_required = u'Solicitante'
    model = PedidoCompra
    template_name = 'fluxo/listas/lista-pc.html'

    def get_queryset(self):
        # pega todos os objetos em pedido de compra e atribui a object_list, usada na lista html, para fazer o filtro do status
        self.object_list = PedidoCompra.objects.filter(usuario_log=self.request.user).filter(status_oc='ABE')

        return self.object_list

# criar
class PCCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'Solicitante'
    model = PedidoCompra
    fields=['data_solic','setor_oc','desc_solic','motivo_solic',
            'valor_solic','anexos','etapa_oc','status_oc'
    ]
    template_name = 'fluxo/form-cad.html'
    success_url = reverse_lazy('lista-pc')

    # para salvar o usuario_log (e todos os demais campos) sem precisar selecionar em uma caixa de seleção para usuario, neste caso
    def form_valid(self, form):

        # antes do super(), o objeto ainda não foi criado, onde será feito o script para salvar o usuario logado no campo usuario_log
        form.instance.usuario_log = self.request.user

        url = super().form_valid(form)

        # objeto já criado 
        return url

# atualizar
class PCUpdate(GroupRequiredMixin, LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'Solicitante'
    model = PedidoCompra
    fields=['setor_oc','desc_solic','motivo_solic',
            'valor_solic','anexos','etapa_oc','status_oc'
    ]
    template_name = 'fluxo/form-cad.html'
    success_url = reverse_lazy('lista-pc')

# apagar
class PCDelete(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'Solicitante'
    model = PedidoCompra
    template_name = 'fluxo/form-excl.html'
    success_url = reverse_lazy('lista-pc')