from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from django.views.generic import TemplateView
from comprador.forms import PedidoForm
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.urls import reverse
from comprador.models import Comprador, EstoqueComprador, Pedido
from distribuidor.models import Distribuidor, EstoqueDistribuidor
from django.urls import reverse

class PedidoView(TemplateView):
    template_name = "pedido.html"


class ListagemView(TemplateView):
    template_name = "lista_for.html"



class PedidoView(CreateView):
    model = Pedido
    template_name = "pedido.html"
    form_class = PedidoForm
    #success_url = 'http://127.0.0.1:8000/comprador/listagem/'
    success_url = 'comprador:litar_fornecedores_p'

    def form_valid(self, form):
        qual_seu_pedido = form.cleaned_data['qual_seu_pedido']
        qual_quantidade_de_unidade = form.cleaned_data['qual_quantidade_de_unidade']
        
        print(qual_seu_pedido)

        self.request.session['quantidade_pedido'] = qual_quantidade_de_unidade
        self.request.session['nome_pedido'] = qual_seu_pedido
        #self.request.session['pedido'] = self
        #cheese_blog = Blog.objects.get(name="Cheddar Talk")
        #print(form)
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()

        return super().form_valid(form)

    def get_success_url(self):
        self.request.session['pedido'] = self.object.pk
        
        return reverse(self.success_url)

class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = "pedido.html"
    form_class = PedidoForm
    #success_url = 'http://127.0.0.1:8000/comprador/listagem/'
    success_url = 'landpage:home'

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        try:
            obj = Pedido.objects.get(pk=self.request.session['pedido'])
        except:
            raise Http404("Pedido não localizado")
        return obj
    # def get_object(self, queryset=None):
    #     slug = self.kwargs.get(self.slug_url_kwarg)
    #     try:
    #         obj = ClientePF.objects.get(slug=slug, empresa=self.request.session['empresa'])
    #     except:
    #         raise Http404("Cliente não localizado")
    #     return obj


    def form_valid(self, form):

        return super().form_valid(form)

    def get_success_url(self):
        return reverse(self.success_url)



class CompradorCreateView(CreateView):
    model = Comprador
    template_name = "comprador_form.html"
    fields = ['nome_comprador', 'email', 'tel_fixo','tel_celular','cep','cidade','lat','lon']
    success_url = 'landpage:home'

    def get_success_url(self):
        return reverse(self.success_url)


class EstoqueCreateView(CreateView):
    model = EstoqueComprador
    template_name = "estoque_form.html"
    fields = ['comprador', 'nome_produto', 'quantidade_em_estoque']
    success_url = 'comprador:p'

    def get_success_url(self):
        return reverse(self.success_url)


class EstoqueListView(CreateView):
    template_name = "estoque_list.html"


class HomeView(TemplateView):
    template_name = 'comprador_home.html'


#class PedidoCreateView(CreateView):
#    model = Pedido
#    form_class = ClientePFForm
#    template_name = 'fazer_pedido_form.html'  

#from django.shortcuts import redirect
class PedidoUpdateEstoque(UpdateView):
    model = Pedido
    template_name = 'receber_pedido_form.html'
#



class LitarPedidoCliente(ListView):
    model = Pedido
    template_name = 'cliente_list_pedido.html'


class LitarFornecedoresP(ListView):
    model = Distribuidor
    template_name = 'fornecedor_list_pedido.html'

    # def get_context_data(self, **kwargs):
    #     context = super(LitarFornecedoresP, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         context['Pedido'] = Pedido.objects.all()
'''
    #     return context
   def get_queryset(self):
        estoque_distri = EstoqueDistribuidor.objects.filter(quantidade_em_estoque__gte=self.request.session['quantidade_pedido'],nome_produto__icontains=self.request.session['nome_pedido'])
        #self.request.session['quantidade_pedido'] = qual_quantidade_de_unidade
        #self.request.session['nome_pedido'] = qual_seu_pedido
        
        #palavra_chave = form.cleaned_data['palavra_chave']
        #tipo = form.cleaned_data['tipo']
        #situacao = form.cleaned_data['situacao']
        #categoria = form.cleaned_data['categoria']
        if self.request.GET:
            qs = super(LitarFornecedoresP, self).get_queryset().filter()
            t = estoque_distri
        else:
            qs = super(LitarFornecedoresP, self).get_queryset().filter()
            t = estoque_distri
        return t
'''