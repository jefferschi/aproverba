from django.urls import path

from .views import VerbaList, VerbaCreate, VerbaUpdate, VerbaDelete
from .views import PCList, PCCreate, PCUpdate, PCDelete, PCEnvia
from .views import PCAprovaList, PCAnaliseAprov, PCAprova
from .views import PCFisList, PCAnaliseFis, PCAprovaFis
from .views import PCFinList, PCAnaliseFin

urlpatterns = [

    # verbas
    path('verbas/listar/', VerbaList.as_view(), name='lista-verbas'),
    path('verbas/cadastrar/',VerbaCreate.as_view(), name='cad-verbas'),
    path('verbas/alterar/<int:pk>/', VerbaUpdate.as_view(), name='alter-verbas'),
    path('verbas/excluir/<int:pk>/', VerbaDelete.as_view(), name='excl-verbas'),

    # pedidos de compra para o solicitante
    path('pc/listar/', PCList.as_view(), name='lista-pc'),
    path('pc/cadastrar/', PCCreate.as_view(), name='cad-pc'),
    path('pc/alterar/<int:pk>/', PCUpdate.as_view(), name='alter-pc'),
    path('pc/excluir/<int:pk>/', PCDelete.as_view(), name='excl-pc'),
    path('pc/enviar/<int:pk>/', PCEnvia.as_view(), name='envia-pc'),

    # análises de PCs para aprovador
    path('pc/analise/aprova/listar/', PCAprovaList.as_view(), name='lista-analise-pc'),
    path('pc/analise/aprova/<int:pk>', PCAnaliseAprov.as_view(), name='analise-aprova-pc'),
    path('pc/analise/aprova/enviar/<int:pk>/', PCAprova.as_view(), name='envia-aprova-pc'),

    # análises de PCs para fiscal
    path('pc/analise/fiscal/listar/', PCFisList.as_view(), name='lista-analise-fis-pc'),
    path('pc/analise/fiscal/<int:pk>', PCAnaliseFis.as_view(), name='analise-fis-pc'),
    path('pc/analise/fiscal/enviar/<int:pk>/', PCAprovaFis.as_view(), name='envia-fis-pc'),

    # análises de PCs para financeiro
    path('pc/analise/financeiro/listar/', PCFinList.as_view(), name='lista-analise-fin-pc'),
    path('pc/analise/financeiro/<int:pk>', PCAnaliseFin.as_view(), name='analise-fin-pc'),

]