// Import the Google Maps JavaScript API
(g => {
    var h, a, k, p = "The Google Maps JavaScript API", c = "google", l = "importLibrary", q = "__ib__", m = document, b = window; b = b[c] || (b[c] = {}); var d = b.maps || (b.maps = {}), r = new Set, e = new URLSearchParams, u = () => h || (h = new Promise(async (f, n) => {
        await (a = m.createElement("script")); e.set("libraries", [...r] + ""); for (k in g) e.set(k.replace(/[A-Z]/g, t => "_" + t[0].toLowerCase()), g[k]); e.set("callback", c + ".maps." + q); a.src = `https://maps.${c}apis.com/maps/api/js?` + e; d[q] = f; a.onerror = () => h = n(Error(p + " could not load.")); a.nonce = m.querySelector("script[nonce]")?.nonce || ""; m.head.append(a)
    })); d[l] ? console.warn(p + " only loads once. Ignoring:", g) : d[l] = (f, ...n) => r.add(f) && u().then(() => d[l](f, ...n))
})
    ({ key: API_KEY, v: "weekly" });

// Initialize and add the map
let map;
async function initMap() {
    // The location of center of the map, currently set to Ireland
    const center = { "lat": 53.4129, "lng": -8.2439 }

    // Request needed libraries.
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    // Create an info window to share between markers.
    const infoWindow = new google.maps.InfoWindow();

    // The map, centered at Uluru
    map = new Map(document.getElementById("map"), {
        zoom: 2, // Adjust the zoom level as needed
        center: center,
        mapId: "DEMO_MAP_ID",
    });


    for (const [city, coordinates] of Object.entries(positions)) {
        const marker = new AdvancedMarkerElement({
            map: map,
            position: coordinates,
            title: city,
            gmpClickable: true,
        });
        marker.addListener("click", () => {
            infoWindow.close();
            infoWindow.setContent(marker.title);
            infoWindow.open(marker.map, marker);
        });
    }
}
initMap();