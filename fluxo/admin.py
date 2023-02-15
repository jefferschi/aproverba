from django.contrib import admin

# Register your models here.
from .models import Setor, Verba, PedidoCompra

# Register your models here.
admin.site.register(Setor)
admin.site.register(Verba)
admin.site.register(PedidoCompra)