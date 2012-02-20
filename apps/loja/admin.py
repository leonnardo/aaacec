# -*- coding:utf-8 -*-
from apps.loja.models import Encomenda,Produto,CategoriaProduto,Campo
from django.contrib import admin
from django import forms
    

class CampoInline(admin.StackedInline):
    model = Campo
    extra = 1
    #def clean_lista()

class EncomendaAdmin(admin.ModelAdmin):
    inlines = (CampoInline,)
    
    list_display = ('nome','produto','abertura','encerramento','campos')

admin.site.register(Encomenda,EncomendaAdmin)
admin.site.register(Produto)
admin.site.register(CategoriaProduto)