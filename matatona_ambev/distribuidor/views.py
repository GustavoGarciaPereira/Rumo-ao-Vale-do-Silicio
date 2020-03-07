from django.urls import path

from .views import EmpresaListView, EmpresaDetailView, EmpresaUpdateView

app_name = 'empresa'
urlpatterns = [
    path('listar', EmpresaListView.as_view(), namespace="list"),

]