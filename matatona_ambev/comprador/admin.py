from django.contrib import admin

# Register your models here.
from comprador.models import Pedido
#from comprador.models import Pe


class PedidoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pedido, PedidoAdmin)


#class EstoqueAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Estoque, EstoqueAdmin)
