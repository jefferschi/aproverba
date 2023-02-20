from django.urls import path

from .views import VerbaList, VerbaCreate, VerbaUpdate, VerbaDelete
from .views import PCList, PCCreate, PCUpdate, PCDelete, PCEnvia
from .views import PCAnaliseList

urlpatterns = [

    # verbas
    path('verbas/listar/', VerbaList.as_view(), name='lista-verbas'),
    path('verbas/cadastrar/',VerbaCreate.as_view(), name='cad-verbas'),
    path('verbas/alterar/<int:pk>/', VerbaUpdate.as_view(), name='alter-verbas'),
    path('verbas/excluir/<int:pk>/', VerbaDelete.as_view(), name='excl-verbas'),

    # pedidos de compra
    path('pc/listar/', PCList.as_view(), name='lista-pc'),
    path('pc/cadastrar/', PCCreate.as_view(), name='cad-pc'),
    path('pc/alterar/<int:pk>/', PCUpdate.as_view(), name='alter-pc'),
    path('pc/excluir/<int:pk>/', PCDelete.as_view(), name='excl-pc'),
    path('pc/enviar/<int:pk>/', PCEnvia.as_view(), name='envia-pc'),

    # análises de PCs
    path('pc/analise/listar/', PCAnaliseList.as_view(), name='lista-analise-pc'),
]