from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView




class PedidoView(TemplateView):
    template_name = "pedido.html"


class ListagemView(TemplateView):
    template_name = "lista_for.html"

from comprador.forms import PedidoForm
from django.views.generic.edit import FormView

class PedidoView(FormView):
    template_name = "pedido.html"
    form_class = PedidoForm
    success_url = 'http://127.0.0.1:8000/comprador/listagem/'

    def form_valid(self, form):
        qual_seu_pedido = form.cleaned_data['qual_seu_pedido']
        qual_quantidade_de_unidade = form.cleaned_data['qual_quantidade_de_unidade']
        print(qual_seu_pedido)
        print(qual_quantidade_de_unidade)
        #print(form)
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        

        return super().form_valid(form)
