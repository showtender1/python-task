from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def show_map():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

        <!-- Leaflet and Plugins -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
        <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>

        <style>
            html, body { width: 100%; height: 100%; margin: 0; padding: 0; }
            #map { position: absolute; top: 0; bottom: 0; right: 0; left: 0; }
            .leaflet-container { font-size: 1rem; }
        </style>
    </head>
    <body>
        <div id="map" class="folium-map"></div>
        <script>
            var map = L.map('map').setView([51.505, -0.09], 13);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '© OpenStreetMap contributors'
            }).addTo(map);

            // Function to add a marker on map click
            map.on('click', function(e) {
                var newMarker = L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);
                newMarker.bindPopup('New Marker at: ' + e.latlng.lat.toFixed(4) + ', ' + e.latlng.lng.toFixed(4)).openPopup();
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
