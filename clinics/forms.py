from django import forms
from .models import Clinic
from geopy.geocoders import Nominatim

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['nome', 'endereco','cidade','telefone']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-duverde focus:border-duverde'
            })
    
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