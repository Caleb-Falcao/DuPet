from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['nome','especie','raca', 'data_nascimento', 'peso', 'foto', 'observacoes']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
        
