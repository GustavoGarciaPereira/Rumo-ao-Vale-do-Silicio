from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView




class PedidoView(TemplateView):
    template_name = "pedido.html"
