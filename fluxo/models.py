from django.db import models
from django.utils import timezone

# para fazer a relação dos filtros com o usuário logado
from django.contrib.auth.models import User

# função para retornar uma string com o caminho do anexo considerando o número da id do objeto e nome do arquivo
def anexar_em(instance, filename):
    return 'anexos/{0}/{1}'.format(instance.id, filename)

class Setor(models.Model):
    # colocar um campo para receber o responsável pelo setor, esse campo vai buscar da tabela usuários padrão do django
    setor_desc = models.CharField(verbose_name='Setor', max_length=100, unique=True)

    def __str__(self):
        return self.setor_desc


class Verba(models.Model):
    data_verba = models.DateTimeField(verbose_name='Data Lançamento', default=timezone.now)
    valor_verba = models.DecimalField(verbose_name='Valor da Verba', max_digits=9, decimal_places=2)
    setor_verba = models.ForeignKey(Setor, on_delete=models.PROTECT, verbose_name='Setor')
    desc_verba = models.CharField(verbose_name='Descrição', max_length=200)
    motivo_verba = models.TextField(verbose_name='Motivo', max_length=1000, blank=True, null=True)

    def __str__(self):
        return "Verba #{} - {} ({})".format(str(self.id),self.desc_verba, self.setor_verba)

    """ atriui a uma variável o nome da classe. Isso pode ser usado em um template para identificar a 
    classe que está chamando o formulário e condicionar as ações"""
    def nome_classe(self):
        nome_modelo = Verba()
        nome_da_classe = nome_modelo._meta.model_name
        return nome_da_classe


class PedidoCompra(models.Model):
    # para a constante abaixo e demais para models.Charfield(choices), ver melhor prática em https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices
   
    SOL = '1'
    APR = '2'
    FIS = '3'
    FIN = '4'
    FIM = '9'
    ETAPAS_CHOICES = [
        (SOL,'Solicitação'),
        (APR,'Aprovação'),
        (FIS,'Fiscal'),
        (FIN,'Financeiro'),
        (FIM,'Finalizada'),
    ]
    
    # para a constante abaixo e demais para models.Charfield(choices), ver melhor prática em https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices

    ABERTA = 'ABE'
    ANALISE = 'ANL'
    LIBERADA = 'LIB'
    NEGADA = 'NEG'
    CANCELADA = 'CAN'
    STATUS_CHOICES = [
        ('ABE','Aberta'),
        ('ANL','Análise'),
        ('LIB','Liberada'),
        ('NEG','Negada'),
        ('CAN','Cancelada'),
    ]

    data_solic = models.DateTimeField(verbose_name='Data da Solicitação', default=timezone.now)
    usuario_log = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário') #deixar este usuário, que herda do padrão django
    setor_oc = models.ForeignKey(Setor, on_delete=models.PROTECT, verbose_name='Setor')
        
    desc_solic = models.CharField(max_length=100, verbose_name='Descrição do pedido')
    motivo_solic = models.TextField(verbose_name='Motivo do pedido', max_length=1000, help_text='Escreva detalhes da solicitação')
    valor_solic = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Valor Solicitado')
    anexos = models.FileField(upload_to=anexar_em, blank=True, null=True)  # verificar melhor como se configura, inclusive a constante MEDDIA_ROOT
    
    data_aprov = models.DateTimeField(verbose_name='Aprovação Diretoria', blank=True, null=True)
    motivo_aprov = models.TextField(verbose_name='Motivo Aprovação', blank=True, max_length=1000, help_text='Escreva detalhes da devolutiva')
    valor_aprov = models.DecimalField(verbose_name='Valor Aprovado', max_digits=9, decimal_places=2, blank=True, null=True)

    data_fin = models.DateTimeField(verbose_name='Liberação Financeiro', blank=True, null=True)
    motivo_fin = models.TextField(verbose_name='Motivo Financeiro', max_length=1000, blank=True, help_text='Escreva detalhes da devolutiva')

    data_fis = models.DateTimeField(verbose_name='Liberação Fiscal', blank=True, null=True)
    motivo_fis = models.TextField(verbose_name='Motivo Fiscal', max_length=1000, blank=True, null=True, help_text='Escreva detalhes da devolutiva')

    etapa_oc = models.CharField(verbose_name='Etapa', choices=ETAPAS_CHOICES, max_length=50)
    status_oc = models.CharField(verbose_name='Status', choices=STATUS_CHOICES, max_length=50)

    data_fim_oc = models.DateTimeField(verbose_name='Data Encerramento', null=True, blank=True)


    def __str__(self):
        return "OC #{} - Solicitação para {}".format(self.id,self.setor_oc)
    
    """ atriui a uma variável o nome da classe. Isso pode ser usado em um template para identificar a 
    classe que está chamando o formulário e condicionar as ações"""
    def nome_classe(self):
        nome_modelo = PedidoCompra()
        nome_da_classe = nome_modelo._meta.model_name
        return nome_da_classe
