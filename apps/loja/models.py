# -*- coding: utf-8 -*-
#models.py - loja
from  django.db.models import *
from django.contrib.auth.models import User


class CategoriaProduto(Model):
    nome = CharField(max_length=50)
    def __unicode__(self):
        return self.nome
    
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
    
    def campos(self):
        lista = Campo.objects.filter(encomenda__id=self.id)
        string = ''
        for elem in lista[:len(lista)-1]:
            string += str(elem)+', '
        string += str(lista[len(lista)-1])
        return string

class Pedido(Model):
    #externos
    usuario = ForeignKey(User,verbose_name='Usuário')
    encomenda = ForeignKey(Encomenda)

    def __unicode__(self):
        return str(self.usuario)+" -> "+str(self.encomenda)

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
    lista = TextField(blank=True, null=True,help_text=u"Apenas válido para tipo == 'lista'. Digite uma opção por linha.")
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
    pedido = ForeignKey(Pedido)
    campo = ForeignKey(Campo)
    
    #metodos
    def __unicode__(self):
        return self.usuario.username+":"+self.valor
    
