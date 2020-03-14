from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from comprador.forms import PedidoForm
from django.views.generic.edit import FormView, CreateView

from comprador.models import Comprador, Estoque


class PedidoView(TemplateView):
    template_name = "pedido.html"


class ListagemView(TemplateView):
    template_name = "lista_for.html"



class PedidoView(FormView):
    template_name = "pedido.html"
    form_class = PedidoForm
    success_url = 'http://127.0.0.1:8000/comprador/listagem/'

    def form_valid(self, form):
        qual_seu_pedido = form.cleaned_data['qual_seu_pedido']
        qual_quantidade_de_unidade = form.cleaned_data['qual_quantidade_de_unidade']
        print(qual_seu_pedido)
        print(qual_quantidade_de_unidade)
        #cheese_blog = Blog.objects.get(name="Cheddar Talk")
        #print(form)
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        return super().form_valid(form)

class CompradorCreateView(CreateView):
    model = Comprador
    template_name = "comprador_form.html"
    fields = ['nome_comprador', 'email', 'tel_fixo','tel_celular','cep','cidade','lat','lon']
    success_url = 'landpage:home'

    def get_success_url(self):
        return reverse(self.success_url)


class EstoqueCreateView(CreateView):
    model = Estoque
    template_name = "estoque_form.html"
    fields = ['comprador', 'nome_produto', 'quantidade_em_estoque']
    success_url = 'comprador:p'

    def get_success_url(self):
        return reverse(self.success_url)


class EstoqueListView(CreateView):
    template_name = "estoque_list.html"


class HomeView(TemplateView):
    template_name = 'comprador_home.html'