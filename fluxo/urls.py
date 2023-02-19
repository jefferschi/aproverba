from django.urls import path

from .views import VerbaList

urlpatterns = [
    path('verbas/listar/', VerbaList.as_view(), name='lista-verbas'),
]