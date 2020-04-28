from django.db import models
import os
from django.utils.translation import ugettext_lazy as _
#from brutils import cpf as valida_cpf, cnpj as valida_cnpj

from django.urls import reverse
# Create your models here.
class Distribuidor(models.Model):
    nome_distribuidor = models.CharField(max_length=30)
    lat = models.DecimalField(max_digits=8, decimal_places=6, verbose_name= 'Latitude')
    lon = models.DecimalField(max_digits=8, decimal_places=6, verbose_name= 'Longitude')
    tel_fixo = models.CharField(_('Telefone Fixo'), max_length=13, blank=True, null=True)
    tel_celular = models.CharField(_('Telefone Celular'), max_length=13, blank=True, null=True)
    cep = models.CharField(_('CEP'), max_length=10, blank=True, null=True)
    uf = models.CharField(_('UF'), max_length=2, blank=True, null=True)
    cidade = models.CharField(_('Cidade'), max_length=70, blank=True, null=True)
    bairro = models.CharField(_('Bairro'), max_length=70, blank=True, null=True)
    logradouro = models.CharField(_('Logradouro'), max_length=70, blank=True, null=True)
    numero = models.CharField(_('Número'), max_length=5, blank=True, null=True)
    complemento = models.CharField(_('Complemento'), max_length=70, blank=True, null=True)
    dt_cadastro = models.DateTimeField(_('Dt. Cadastro'), auto_now_add=True)
    email = models.EmailField(_('E-mail'), blank=True, null=True)
    
    inicio_hora_entrega = models.TimeField(_('Inicio Periodo Entrada'),auto_now=False, auto_now_add=False,blank=True,
    null=True)
    fim_hora_entrega = models.TimeField(_('Fim Periodo Entrada'),auto_now=False, auto_now_add=False,blank=True,
    null=True)
    def __str__(self):
        return self.nome_distribuidor
    

class EstoqueDistribuidor(models.Model):
    distribuidor = models.ForeignKey(Distribuidor,on_delete=models.PROTECT)
    nome_produto = models.CharField(max_length=30) 
    quantidade_em_estoque = models.IntegerField(blank=True, null=True)

    @property
    def get_absolute_url2(self):
        return reverse('comprador:finalizar_pedido_up', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
            
        super(EstoqueDistribuidor, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome_produto
    