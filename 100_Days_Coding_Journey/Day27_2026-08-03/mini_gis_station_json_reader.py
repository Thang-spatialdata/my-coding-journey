import json

stations = [
    {"name": "HY01", "temp": 28, "coords": [105.85, 21.03]},
    {"name": "HY02", "temp": 31, "coords": [106.68, 20.85]},
    {"name": "HY03", "temp": 25, "coords": [106.20, 20.60]}
]


# Save JSON file
with open("stations.json", "w") as f:
    json.dump(stations, f)


# Load JSON file
with open("stations.json", "r") as f:
    loaded_stations = json.load(f)


# Print station coordinates
for station in loaded_stations:
    name = station["name"]
    coords = station["coords"]
    print(f"{name} at {coords}")


# Find hottest station
hottest_station = loaded_stations[0]

for station in loaded_stations:
    if station["temp"] > hottest_station["temp"]:
        hottest_station = station

print(f"Hottest station: {hottest_station['name']}")
