from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from .views import distribuidorCreateView,ListagemView

app_name = 'distribuidor'
urlpatterns = [
    path('cadastrar/', distribuidorCreateView.as_view(), name='distribuidor_create'),
    path('listar/', ListagemView.as_view(), name='distribuidor_list'),
]