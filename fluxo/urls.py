from django.urls import path

from .views import VerbaList, VerbaCreate

urlpatterns = [
    path('verbas/listar/', VerbaList.as_view(), name='lista-verbas'),
    path('verbas/cadastrar/',VerbaCreate.as_view(), name='cad-verbas'),
]