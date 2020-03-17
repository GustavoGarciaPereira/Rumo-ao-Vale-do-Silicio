from django.urls import path
from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
from django.conf import settings

from .models import Distribuidor, EstoqueDistribuidor

class HomeView(TemplateView):
    template_name = 'distribuidor_home.html'

class distribuidorCreateView(CreateView):
    model = Distribuidor
    template_name = "distribuidor_form.html"
    fields = ['nome_distribuidor', 'email', 'tel_fixo','tel_celular','cep','cidade','lat','lon']
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
