from django.shortcuts import render, redirect
from .models import Clinic
from .forms import ClinicForm
from django.http import JsonResponse
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import requests
from django.conf import settings

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'clinics/clinic_list.html', {
        'clinics': clinics,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })


def clinic_add(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST)
        if form.is_valid():
            clinic = form.save(commit=False)
            
            # Geolocalização
            geolocator = Nominatim(user_agent="dupet")
            location = geolocator.geocode(f"{clinic.endereco}, {clinic.cidade}")
            
            if location:
                clinic.latitude = location.latitude
                clinic.longitude = location.longitude

            clinic.save()
            return redirect('clinic_list')
    else:
        form = ClinicForm()
    return render(request, 'clinics/clinic_form.html', {'form': form})

def clinics_nearby(request):
    try:
        user_lat = float(request.GET.get('lat'))
        user_lon = float(request.GET.get('lon'))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Parâmetros inválidos'}, status=400)
    
    #clinics = Clinic.objects.all()
    #nearby = []
    
    #google api maps
    GOOGLE_API_KEY = settings.GOOGLE_MAPS_API_KEY

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": f"{user_lat},{user_lon}",
        "radius": 5000,  # 5km
        "type": "veterinary_care",
        "key": GOOGLE_API_KEY,
        "language": "pt-BR"
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    # Filtra campos relevantes
    results = []
    for place in data.get("results", []):
        results.append({
            "nome": place.get("name"),
            "endereco": place.get("vicinity"),
            "latitude": place["geometry"]["location"]["lat"],
            "longitude": place["geometry"]["location"]["lng"],
            "nota": place.get("rating"),
        })

    return JsonResponse(results, safe=False)
    """
    for clinic in clinics:
        if clinic.latitude is not None and clinic.longitude is not None:
            try:
                dist = geodesic((user_lat, user_lon), (clinic.latitude, clinic.longitude)).km
                if dist <= 10:  # raio de 10km
                    nearby.append({
                        'nome': clinic.nome,
                        'endereco': clinic.endereco,
                        'cidade': clinic.cidade,
                        'distancia_km': round(dist, 2),
                    })
            except Exception as e:
                continue  # se der erro em algum, pula

    return JsonResponse(nearby, safe=False)
    """
    
    
