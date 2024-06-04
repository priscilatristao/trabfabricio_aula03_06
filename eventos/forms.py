# eventos/forms.py
from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'data_inicio', 'hora_inicio', 'data_final', 'hora_final', 'local', 'criador']
