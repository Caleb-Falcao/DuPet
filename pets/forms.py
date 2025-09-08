from django import forms
from .models import Pet

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
