# -*- coding: utf-8 -*-
from django.forms import *

from apps.loja.models import Pedido,Campo,Info

class PedidoForm(Form):

    def __init__(self,encomenda, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
      
        campos = Campo.objects.filter(
            encomenda=encomenda)
        
        for campo in campos:
            if campo.tipo == 'texto':
                self.fields[campo.nome] = CharField(
                                                required=campo.obrigatorio)
            elif campo.tipo == 'numero':
                self.fields[campo.nome] = IntegerField(
                                                required=campo.obrigatorio)
            elif campo.tipo == 'decimal':
                self.fields[campo.nome] = DecimalField(
                                                required=campo.obrigatorio)
            elif campo.tipo == 'bool':
                self.fields[campo.nome] = BooleanField(
                                                required=campo.obrigatorio)
            elif campo.tipo == 'lista':
                choices = [ (x,x) for x in campo.lista.split('\n')]
                self.fields[campo.nome] = ChoiceField(
                                                required=campo.obrigatorio,
                                                choices=choices)

    def save(self,encomenda,usuario):
        ''' função que gerará o objeto Pedido com as respectivas Infos no banco'''
        
        pedido = Pedido(
            encomenda=encomenda,
            usuario=usuario)
        pedido.save()

        campos = Campo.objects.filter(
            encomenda=encomenda)

        print self.__dict__
        for campo in campos:

            i = Info(
                campo=campo,
                pedido=pedido,
                valor=self.cleaned_data[campo.nome]
                )
            i.save()
