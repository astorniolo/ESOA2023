from django.contrib import admin
from gestorPedidos.models import Cliente,Articulos,Pedidos

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Articulos)
admin.site.register(Pedidos)