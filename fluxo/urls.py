from django.urls import path

from .views import VerbaList, VerbaCreate, VerbaUpdate

urlpatterns = [
    path('verbas/listar/', VerbaList.as_view(), name='lista-verbas'),
    path('verbas/cadastrar/',VerbaCreate.as_view(), name='cad-verbas'),
    path('verbas/alterar/<int:pk>/', VerbaUpdate.as_view(), name='alter-verbas'),
]