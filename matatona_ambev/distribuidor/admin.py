from django.contrib import admin

# Register your models here.
from .models import Distribuidor, EstoqueDistribuidor

class DistribuidorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Distribuidor, DistribuidorAdmin)


class EstoqueAdmin(admin.ModelAdmin):
    pass
admin.site.register(EstoqueDistribuidor, EstoqueAdmin)
