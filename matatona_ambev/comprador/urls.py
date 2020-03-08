

from django.contrib import admin
from django.urls import include, path
from .views import PedidoView




app_name = 'comprador'

urlpatterns = [

    path('pedido/', PedidoView.as_view(), name='p'),
]
