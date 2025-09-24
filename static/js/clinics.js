function buscarClinicasGoogle() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((position) => {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      const location = new google.maps.LatLng(lat, lon);

      const service = new google.maps.places.PlacesService(document.createElement('div'));

      service.nearbySearch({
        location: location,
        radius: 5000,
        keyword: 'clínica veterinária'
      }, (results, status) => {
        const container = document.getElementById('google-clinics');
        container.innerHTML = '';

        if (status !== google.maps.places.PlacesServiceStatus.OK || results.length === 0) {
          container.innerHTML = '<p class="text-gray-500">Nenhuma clínica encontrada próxima.</p>';
          return;
        }

        results.forEach(place => {
          const item = document.createElement('div');
          item.className = "border rounded p-4 shadow bg-white";
          item.innerHTML = `
            <h3 class="text-green-700 font-semibold">${place.name}</h3>
            <p class="text-sm text-gray-600">${place.vicinity || 'Endereço não disponível'}</p>
          `;
          container.appendChild(item);
        });
      });
    }, () => {
      alert('Permita o acesso à sua localização.');
    });
  } else {
    alert('Seu navegador não suporta geolocalização.');
  }
}
