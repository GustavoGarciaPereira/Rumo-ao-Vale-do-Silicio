from django.contrib import admin

# Register your models here.
from .models import Distribuidor, Estoque

class DistribuidorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Distribuidor, DistribuidorAdmin)


class EstoqueAdmin(admin.ModelAdmin):
    pass
admin.site.register(Estoque, EstoqueAdmin)
