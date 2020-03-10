from django import forms

class PedidoForm(forms.Form):
    qual_seu_pedido = forms.CharField(label='Informe aqui o seu pedido', max_length=100)
    qual_quantidade_de_unidade = forms.IntegerField(label='Informe aqui a quantidade de unidade')