#from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# modelos do projeto
from .models import Verba, PedidoCompra, Setor

# para requerer login ao acessar as páginas, mesmo digitando o endereço no navegador
from django.contrib.auth.mixins import LoginRequiredMixin

# para gerenciar permissões por grupos. Pode ser feito pelo gerenciador do djaango, mas aqui será pelo braces
from braces.views import GroupRequiredMixin

# redireciona o usuário depois de fazer algo
from django.urls import reverse_lazy

from django.utils import timezone


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
""" classes para Pedidos de Compra nível de acesso 'Solicitante' -  ListView, CreteView, UpdateView, DeleteView, """

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
    fields=['desc_solic','motivo_solic',
            'valor_solic','anexos'
    ]
    template_name = 'fluxo/form-cad.html'
    success_url = reverse_lazy('lista-pc')

    # para salvar o usuario_log (e todos os demais campos) sem precisar selecionar em uma caixa de seleção para usuario, neste caso
    def form_valid(self, form):

        # antes do super(), o objeto ainda não foi criado, onde será feito o script para salvar o usuario logado no campo usuario_log

        # recebe o usuário logado no campo usuário do pedido
        form.instance.usuario_log = self.request.user

        # recebe o setor do usuário logado, referente ao gestor do setor no cadastro de setor
        setor = Setor.objects.get(gestor_setor=self.request.user)
        # Define o valor do campo setor_oc como o setor encontrado
        form.instance.setor_oc = setor

        url = super().form_valid(form)

        # objeto já criado 
        return url

# atualizar
class PCUpdate(GroupRequiredMixin, LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'Solicitante'
    model = PedidoCompra
    fields=['setor_oc','desc_solic','motivo_solic',
            'valor_solic','anexos'
    ]
    template_name = 'fluxo/form-cad.html'
    success_url = reverse_lazy('lista-pc')

    # colocar uma função para salvar a data toda vez que alterar o registro.

# apagar
class PCDelete(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'Solicitante'
    model = PedidoCompra
    template_name = 'fluxo/form-excl.html'
    success_url = reverse_lazy('lista-pc')

# enviar para análise
class PCEnvia(GroupRequiredMixin, LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'Solicitante'
    model = PedidoCompra
    fields=[]
    template_name = 'fluxo/form-envia-pc.html'
    success_url = reverse_lazy('lista-pc')

    def form_valid(self, form):

        # atribuir a próxima etapa e novo status à oc - vai para aprovação
        form.instance.etapa_oc = '2'
        form.instance.status_oc = 'ANL'

        url = super().form_valid(form)

        # objeto já criado 
        return url


######################################################################################
""" classes para Análise de PCs (aprovação, fiscal e financeiro) """

# lista dos pedidos para aprovação diretoria
class PCAprovaList(GroupRequiredMixin, LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    group_required = u'Aprovador'
    model = PedidoCompra
    template_name = 'fluxo/listas/lista-analise-pc.html'
    
    def get_queryset(self):
        # pega todos os objetos em pedido de compra e atribui a object_list, usada na lista html, para fazer o filtro do status
        self.object_list = PedidoCompra.objects.filter(status_oc='ANL', etapa_oc='2')

        return self.object_list

# detalhes do pedido para aprocação da diretoria
class PCAnaliseAprov(GroupRequiredMixin, LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'Aprovador'
    model = PedidoCompra
    fields=['valor_aprov', 'motivo_aprov'
    ]
    template_name = 'fluxo/form-analise.html'
    success_url = reverse_lazy('lista-analise-pc')

# aprova e envia para Fiscal
class PCAprova(GroupRequiredMixin, LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'Aprovador'
    model = PedidoCompra
    fields=[]
    template_name = 'fluxo/form-aprova-pc.html'
    success_url = reverse_lazy('lista-analise-pc')

    def form_valid(self, form):

        # atribuir a próxima etapa e novo status à oc - vai para fiscal
        form.instance.data_aprov = timezone.now()
        form.instance.etapa_oc = '3'
        form.instance.status_oc = 'LIB'
        

        url = super().form_valid(form)

        # objeto já criado 
        return url