from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from .views import distribuidorCreateView,ListagemView,HomeView
from .views import EstoqueCreateView, EstoqueListView,ListagemCompradoresView
app_name = 'distribuidor'
urlpatterns = [
    path('home/', HomeView.as_view(), name='distribuidor_home'),
    path('cadastrar/', distribuidorCreateView.as_view(), name='distribuidor_create'),
    path('listar/', ListagemView.as_view(), name='distribuidor_list'),
    path('cadastrar_estoque/', EstoqueCreateView.as_view(), name='estoque_create'),
    path('listar_estoque/', EstoqueListView.as_view(), name='estoque_list'),
    path('listar_compradores/', ListagemCompradoresView.as_view(), name='listagem_compradores_list'),
]