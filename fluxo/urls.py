from django.urls import path

from .views import VerbaList, VerbaCreate, VerbaUpdate, VerbaDelete
from .views import PCList

urlpatterns = [
    path('verbas/listar/', VerbaList.as_view(), name='lista-verbas'),
    path('verbas/cadastrar/',VerbaCreate.as_view(), name='cad-verbas'),
    path('verbas/alterar/<int:pk>/', VerbaUpdate.as_view(), name='alter-verbas'),
    path('verbas/excluir/<int:pk>/', VerbaDelete.as_view(), name='excl-verbas'),

    path('pc/listar/', PCList.as_view(), name='lista-pc'),
]