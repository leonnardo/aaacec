# -*- coding: utf-8 -*-

from aaacec.apps.intercomp2012.forms import FormIntercomp
from aaacec.apps.intercomp2012.models import Pacote
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def encomenda(request):

    #verifica se está recebendo informação do form pelo POST
    if request.method != 'POST':
        form = FormIntercomp()
        return render_to_response("intercomp2012/encomenda.html",locals(),context_instance=RequestContext(request))
    
    #pega os dados do POST
    form = FormIntercomp(request.POST)
        
    #verifica se as informações recebidas são válidas
    if not form.is_valid():    
        return render_to_response("intercomp2012/encomenda.html",locals(),context_instance=RequestContext(request))

    #salva os dados do form
    e = form.save(commit=False)
    e.pago = 0
    e.responsavel = "site"
    e.formapag = u"Depósito"
    e.cod_tipo = "Completo"
    e.save()
    
    return HttpResponseRedirect("finalizado")

def fim(request):
    return render_to_response("intercomp2012/fim.html",locals())

def lista(request):
    delegacao = Pacote.objects.all()
    return render_to_response("intercomp2012/lista.html",locals())

def ficha(request, rg):
    pessoa = Pacote.objects.get(rg=rg)
    completo = pessoa.telefone
    ddd = completo[0:2]
    telefone = completo[2:]
    return render_to_response("intercomp2012/ficha.html",locals())
