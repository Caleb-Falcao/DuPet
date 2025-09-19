from django import forms
from .models import Pet, Vacina, Alimentacao, Consulta, Peso

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            "nome",
            "especie",
            "raca",
            "sexo",
            "cor",
            "porte",
            "data_nascimento",     # atualizado
            "peso",     # atualizado
            "microchip",
            "foto",
            "observacoes",
        ]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "peso": forms.NumberInput(attrs={"step": "0.01", "class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        }


class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ["nome", "data_aplicacao", "proxima_dose","veterinario"]
        widgets = {
            "data_aplicacao": forms.DateInput(attrs={"type": "date"}),
            "proxima_dose": forms.DateInput(attrs={"type": "date"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-duverde focus:border-duverde'
            })

class AlimentacaoForm(forms.ModelForm):
    class Meta:
        model = Alimentacao
        fields = ["descricao", "quantidade", "horario"]
        widgets = {
            "horario": forms.TimeInput(attrs={"type": "time"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-duverde focus:border-duverde'
            })
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ["data", "local", "veterinario", "motivo", "observacoes"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-duverde focus:border-duverde'
            })
class PesoForm(forms.ModelForm):
    class Meta:
        model = Peso
        fields = ["peso"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-duverde focus:border-duverde'
            })