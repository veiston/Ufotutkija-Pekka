document.addEventListener("DOMContentLoaded", () => {
    const airportMap = {
        1: ["KBNA"],
        2: ["KDEN", "KSEA", "KHTS"],
        3: ["KBNA"],
        default: ["KDEN", "KSEA", "KBNA", "KHTS"],
    };

    const airportCoordinates = {
        KBNA: [36.1245002746582, -86.6781997680664],
        KDEN: [39.861698150635, -104.672996521],
        KHTS: [38.366699, -82.557999],
        KSEA: [47.449001, -122.308998],
        EFHK: [60.3172, 24.963301],
    };

    const airportNames = {
        KBNA: "Nashville International Airport",
        KDEN: "Denver International Airport",
        KHTS: "Tri-State/Milton J. Ferguson Field",
        KSEA: "Seattle Tacoma International Airport",
        EFHK: "Helsinki Vantaa Airport",
    };

    const airportIcon = L.icon({
        iconUrl:
            "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-black.png",
        shadowUrl:
            "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png",
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41],
    });

    const fetchPlayer = async () => {
        try {
            const response = await fetch("/player/detail");
            return await response.json();
        } catch (error) {
            console.error(error);
            return null;
        }
    };

    const handleAirportClick = async (code, money) => {
        try {
            await new Promise((resolve) => setTimeout(resolve, 500));
            const response = await fetch("/player/update", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({location_ident: code, money}),
            });
            if (!response.ok) throw new Error("Failed to update location");
            window.location.href = "/investigations";
        } catch (error) {
            console.error(error);
        }
    };

    const loadMap = async () => {
        const player = await fetchPlayer();
        if (!player) return;

        const playerLevel = player.player_level;
        const playerMoney = player.money;
        const allowedAirports = airportMap[playerLevel] || airportMap.default;

        const map = L.map("map");

        const currentLocation = player.location_ident;
        const currentCoords = airportCoordinates[currentLocation];
        const bounds = L.latLngBounds([]);

        let currentMarker;
        if (currentCoords) {
            const currentMarkerIcon = L.icon({
                iconUrl:
                    "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png",
                shadowUrl:
                    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png",
                iconSize: [25, 41],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34],
                shadowSize: [41, 41],
            });

            currentMarker = L.marker(currentCoords, {icon: currentMarkerIcon});
            currentMarker.bindPopup(
                `You are here: ${airportNames[currentLocation] || currentLocation}`
            );
            bounds.extend(currentCoords);
        }

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: "© OpenStreetMap contributors",
        }).addTo(map);

        allowedAirports.forEach((code) => {
            const coords = airportCoordinates[code];
            if (!coords) return;

            const marker = L.marker(coords, {icon: airportIcon}).addTo(map);
            marker.bindPopup(
                `${airportNames[code]} (${code})<br>Flight cost: $100`
            );

            marker.on("click", function () {
                if (playerMoney < 100) {
                    showModal({
                        message: `Insufficient funds for the flight. You have $${playerMoney}, but the flight costs $100. Have you tried to earn more money by gambling?`,
                        buttons: [{label: "OK", value: true}],
                    });
                    return;
                }
                const flightLine = L.polyline([currentCoords, coords], {
                    color: "#5C6D89",
                    weight: 5,
                    opacity: 0.8,
                }).addTo(map);
                setTimeout(function () {
                    showModal({
                        message: "This flight costs $100. Do you want to proceed?",
                        buttons: [
                            {label: "Yes", value: true},
                            {label: "No", value: false},
                        ],
                        onClose: function (confirmed) {
                            if (confirmed) {
                                const newMoney = player.money - 100;
                                handleAirportClick(code, newMoney);
                            } else {
                                map.removeLayer(flightLine);
                            }
                        },
                    });
                }, 500);
            });

            bounds.extend(coords);
        });

        if (currentCoords && currentMarker) {
            currentMarker.addTo(map);
        }

        if (bounds.isValid()) {
            map.fitBounds(bounds);
        }
    };

    loadMap();

    document.getElementById("backToMenu").addEventListener("click", () => {
        window.location.href = "/menu";
    });
});