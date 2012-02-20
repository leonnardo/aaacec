from datetime import datetime

from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list,object_detail

from apps.loja.models import Encomenda,Info,Campo,Produto

def index(request):
    return render_to_response('loja/index.html',context_instance=RequestContext(request))
    

def listar_encomendas(request):
    return object_list(
        request,
        Encomenda.objects.filter(
            Q(abertura__lt=datetime.now()) & Q(encerramento__gt=datetime.now())        
        )
    )

@login_required
def fazer_encomenda(request,id):
    
    return render_to_response('loja/encomenda_create.html',context_instance=RequestContext(request))

def cancelar_encomenda(request,id):
    return HttpResponse('Cancelar encomenda')

def checar_encomenda(request,id):
    return HttpResponse('Status da encomenda')
