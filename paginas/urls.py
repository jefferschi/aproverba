from django.urls import path
from .views import PaginaInicial

urlpatterns = [
     # path() exige os argumentos: (endereço, sua_view.as_view(), nome)
    path('',PaginaInicial.as_view(),name='index'),
]