# -*- coding: utf-8 -*-

from datetime import datetime

from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list,object_detail

from apps.loja.models import Encomenda,Info,Campo,Produto,Pedido
from apps.loja.forms import PedidoForm

def index(request):
    return render_to_response(
        'loja/index.html',
        context_instance=RequestContext(request)
    )
    

def listar_encomendas(request):
    
    ''' essa view usa a view genérica para listar as encomendas que existem
    '''

    return object_list(
        request,
        Encomenda.objects.filter(
            Q(abertura__lt=datetime.now()) & Q(encerramento__gt=datetime.now())        
        )
    )

@login_required
def fazer_encomenda(request,id):
    
    encomenda = Encomenda.objects.get(pk=int(id))

    '''primeiro vamos ver se o usuário já fez algum pedido ou se é o seu 
       primeiro pedido para essa encomenda'''

    pedidos = Pedido.objects.filter(
        usuario = request.user,
        encomenda=encomenda
    )

    
    if request.method == 'POST':
        form = PedidoForm(encomenda,request.POST)
        if form.is_valid():
            form.save(encomenda=encomenda,
                    usuario=request.user)

    else:
        form = PedidoForm(encomenda)
    
    if len(pedidos) != 0:
        warning = True
        
    return render_to_response(
        'loja/encomenda_create.html',
        locals(),
        context_instance=RequestContext(request)
    )

def cancelar_encomenda(request,id):
    return HttpResponse('Cancelar encomenda')

def checar_encomenda(request,id):
    return HttpResponse('Status da encomenda')
