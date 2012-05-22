from aaacec.apps.intercomp2012.models import Pacote
from django import forms

class FormIntercomp(forms.ModelForm):
    
    class Meta:
        model = Pacote
        exclude = ['pago', 'responsavel', 'cod_tipo', 'formapag']
        
