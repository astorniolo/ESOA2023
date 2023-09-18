from django.contrib import admin
from gestorPedidos.models import Cliente,Articulos,Pedidos

# Register your models here.

# Para elegir atributos  debo heredar de models.admin
class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","email")
    search_fields=("nombre","email")
    #readonly_fields=("fechaUltimaModificacion")
    ordering=("nombre","email")
    list_filter=("direccion",)
    

    
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)