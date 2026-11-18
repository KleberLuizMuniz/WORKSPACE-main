from django import forms
from sistema.models import *

class ponsultaForm(forms.ModelForm):
    class Meta:
            model = Paciente
            fields = ['nome', 'sobrenome', 'email', 'telefone',]
            # criacao_data e ativo não aparecem: são preenchidos automaticamente.
            labels = {
                'nome': 'Nome',
                'sobrenome': 'Sobrenome',
                'email': 'E-mail',
                'telefone': 'Telefone',
            }