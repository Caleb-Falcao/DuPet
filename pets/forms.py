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
        fields = ["nome", "data_aplicacao","proxima_dose", "veterinario"]

class AlimentacaoForm(forms.ModelForm):
    class Meta:
        model = Alimentacao
        fields = ["descricao", "quantidade", "horario"]

class ConsultaForm(form.ModelForm):
    class Meta:
        model = Consulta
        fields = ["data", "local", "veterinario", "motivo", "observacoes"]
        
class PesoForm(forms.ModelForm):
    class Meta:
        model = Peso
        fields = ["peso"]    