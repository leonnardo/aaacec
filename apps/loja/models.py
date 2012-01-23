# -*- coding: utf-8 -*-
#models.py - loja
from  django.db.models import *
from django.contrib.auth.models import User
class CategoriaProduto(Model):
    nome = CharField(max_length=50)
    
class Produto(Model):
    #internos
    nome = CharField(max_length=50)
    descricao = TextField(verbose_name='Descrição')
    #TODO: adicionar foto do produto
    preco_membro = FloatField()
    preco_naomembro = FloatField()
    
    #externos
    categoria = ManyToManyField(CategoriaProduto)
    
    #metodos
    def __unicode__(self):
        return self.nome
        
class Encomenda(Model):
    #internos
    nome = CharField(max_length=50)
    abertura = DateTimeField()
    encerramento = DateTimeField()
    
    #externos
    produto = ForeignKey(Produto)
    
    #metodos
    def __unicode__(self):
        return self.nome
    
class Campo(Model):
    TIPO_CHOICES =(
        ('texto','Texto'),
        ('numero',u'Número'),
        ('decimal','Decimal'),
        ('lista','Lista'),
        ('bool','Booleano'),
   ) 
    #internos    
    nome = CharField(max_length=50)
    tipo = CharField(max_length=10, choices=TIPO_CHOICES)
    '''
    lista é uma string, separada por virgulas, com cada
    opção de lista, para o caso de tipo == 'lista'
    '''
    lista = TextField(blank=True, null=True)
    obrigatorio = BooleanField(verbose_name=u"Obrigatório")
    #externos
    encomenda = ForeignKey(Encomenda)
    
    #metodos
    def __unicode__(self):
        return self.nome
    
class Info(Model):
    #internos
    valor = CharField(max_length=20)
    
    #externos
    usuario = ForeignKey(User,verbose_name = 'Usuário')
    campo = ForeignKey(Campo)
    
    #metodos
    def __unicode__(self):
        return self.usuario.username+":"+self.valor
    
