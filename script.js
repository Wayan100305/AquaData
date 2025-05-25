const map = L.map('map').setView([0.0, 120.0], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Peta © OpenStreetMap contributors',
}).addTo(map);

fetch('/floaters_position')
  .then((res) => res.json())
  .then((data) => {
    data.forEach((floater) => {
      const lat = floater.position.lat;
      const lng = floater.position.lng;
      const mac = floater.mac_address;

      L.marker([lat, lng])
        .addTo(map)
        .bindPopup(`<b>${mac}</b><br/>ID: ${floater.id}`);
    });
  })
  .catch((err) => {
    alert("Gagal mengambil data dari API.");
    console.error(err);
  });
