

from django.contrib import admin
from django.urls import include, path
from .views import PedidoView, ListagemView, PedidoView, CompradorCreateView, EstoqueCreateView, HomeView, PedidoUpdateEstoque, LitarPedidoCliente


app_name = 'comprador'
urlpatterns = [
    path('pedido/', PedidoView.as_view(), name='p'),
    #path('pedido/', PedidoView.as_view(), name='p'),
    path('listagem/', ListagemView.as_view(), name='list'),
    path('comprador_cadastro/', CompradorCreateView.as_view(), name='create_comprador'),
    path('estoque_compredor/', EstoqueCreateView.as_view(), name='create_estoque'),
    path('home_compredor/', HomeView.as_view(), name='comprador_home'),
    path('receber_pedido/', PedidoUpdateEstoque.as_view(), name='comprador_listar_pedidos'),
    path('lista_pedido_comprador/', LitarPedidoCliente.as_view(), name='comprador_pedido_list')
]

