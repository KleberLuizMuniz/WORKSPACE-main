from django import forms
from sistema.models import *

class consultaForm(forms.ModelForm):
    class Meta:
            model = Consulta
            fields = ['data_consulta', 'ativa', 'observacao', 'status']
                    # criacao_data e ativo não aparecem: são preenchidos automaticamente.
            labels = {
                        'data_consulta' : 'Data',
                        'ativa' : 'Ativa',
                        'observacao' : 'Observação',
                        'status' : 'Status',
                    }