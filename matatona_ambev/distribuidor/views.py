from django.urls import path
from django.views.generic import TemplateView




class PedidoView(TemplateView):
    template_name = "pedido.html"


class ListagemView(TemplateView):
    template_name = "lista_for.html"
