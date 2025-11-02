const map = L.map('map').setView([53.3498, -6.2603], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

fetch('/api/knowledgeplaces/')  // matches the DRF router
  .then(res => res.json())
  .then(data => {
      L.geoJSON(data, {
          pointToLayer: function(feature, latlng) {
              return L.circleMarker(latlng, {
                  radius: 6,
                  color: 'blue',
                  fillOpacity: 0.8
              });
          },
          onEachFeature: function(feature, layer) {
              layer.bindPopup(`<strong>${feature.properties.name}</strong><br>${feature.properties.category}`);
          }
      }).addTo(map);
  })
  .catch(err => console.error('Error loading GeoJSON:', err));
