from django import forms
from .models import Clinic
from geopy.geocoders import Nominatim

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['nome', 'endereco','cidade','telefone']
        
    def save(self, commit=True):
        clinic = super().save(commit=False)
        geolocator = Nominatim(user_agent="dupet_app")
        location = geolocator.geocode(f"{clinic.endereco},{clinic.cidade}")
        
        if location:
            clinic.latitude = location.latitude
            clinic.latitude = location.longitude
        
        if commit:
            clinic.save()
        return clinic