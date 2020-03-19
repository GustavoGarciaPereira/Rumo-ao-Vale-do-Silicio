from django.urls import path
from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
from django.conf import settings

from .models import Distribuidor, EstoqueDistribuidor
from comprador.models import Pedido

class HomeView(TemplateView):
    template_name = 'distribuidor_home.html'

class distribuidorCreateView(CreateView):
    model = Distribuidor
    template_name = "distribuidor_form.html"
    fields = ['fim_hora_entrega','inicio_hora_entrega','nome_distribuidor', 'email', 'tel_fixo','tel_celular','cep','cidade','lat','lon']
    success_url = 'landpage:home'

    def get_success_url(self):
        return reverse(self.success_url)

class EstoqueCreateView(CreateView):
    model = EstoqueDistribuidor
    template_name = "estoque_form.html"
    fields = ['distribuidor', 'nome_produto', 'quantidade_em_estoque']
    success_url = 'distribuidor:distribuidor_home'

    def get_success_url(self):
        return reverse(self.success_url)

class EstoqueListView(CreateView):
    template_name = "estoque_list.html"


class PedidoView(TemplateView):
    template_name = "pedido.html"


class ListagemView(TemplateView):
    template_name = "distribuidor_list.html"

class ListagemCompradoresView(ListView):
    model = Pedido
    template_name = "distribuidor_compradores_list.html"


    #filtrar pelo usuario logado    
    # def get_queryset(self):
    #     queryset = super(SubmissaoListView, self).get_queryset()
    #     queryset = queryset.filter(responsavel = self.request.user)
    #     return queryset
    def get_queryset(self):
        queryset = super(ListagemCompradoresView, self).get_queryset()
        queryset = queryset.filter(distribuidor__id=1)
        return queryset