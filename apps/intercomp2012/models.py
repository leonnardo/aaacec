# -*- coding:utf8 -*-
from django.db import models

PACOTE_CHOICE = ((u"Festa",u"Festa"),(u"Sem festa",u"Sem festa"),(u"Completo",u"Completo"),)
CURSO_CHOICE = (("Engenharia","Engenharia"),(u"Ciência",u"Ciência"),(u"Estat",u"Estat"),(u"Outro",u"Outro"),)
ANO = (("Dino", "Dino"),("2008", "2008"),("2009", "2009"),("2010", "2010"),("2011", "2011"),("2012", "2012"))
MODALIDADES = ((u"Fustal", u"Futsal"), (u"Basquete", u"Basquete"), (u"Handebol", u"Handebol"), (u"Vôlei", u"Vôlei"), (u"Outro", u"Outro"))

class Pacote(models.Model):

	nome = models.CharField(max_length=100)
	nascimento = models.CharField(max_length=8)
	rg = models.CharField(max_length=15)
	emissor = models.CharField(max_length=10)
	ra = models.CharField(max_length=6)
	cpf = models.CharField(max_length=15)
	telefone = models.CharField(max_length=11)
	email = models.CharField(max_length=100)
	curso = models.CharField(verbose_name="Curso", choices=CURSO_CHOICE, max_length=10)
	ano = models.CharField(max_length=4)
	cod_pessoa = models.BooleanField(verbose_name = "Membro/Namorada")
	cod_tipo = models.CharField(verbose_name = "Tipo de pacote",choices=PACOTE_CHOICE, max_length=15)
  	atleta = models.BooleanField(verbose_name = "Atleta?")
    	modalidade = models.CharField(verbose_name="Modalidade", choices=MODALIDADES, max_length=15)
    	formapag = models.CharField(verbose_name="Forma de pagamento", choices=((u"Depósito",u"Depósito"), ("Atendimento","Atendimento")), max_length=15)
    	pago = models.FloatField()
	responsavel = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.nome

	ra.blank = True
	ra.null = True
	modalidade.blank = True
    	modalidade.null = True
