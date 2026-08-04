import json

geo_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "HY01", "temp": 28},
            "geometry": {"coordinates": [105.85, 21.03]}
        },
        {
            "type": "Feature",
            "properties": {"name": "HY02", "temp": 31},
            "geometry": {"coordinates": [106.68, 20.85]}
        },
        {
            "type": "Feature",
            "properties": {"name": "HY03", "temp": None},
            "geometry": {"coordinates": [106.20, 20.60]}
        },
        {
            "type": "Feature",
            "properties": {"name": "HY04", "temp": 35},
            "geometry": {"coordinates": [106.05, 20.95]}
        }
    ]
}


# Save GeoJSON file
with open("map.geojson", "w") as f:
    json.dump(geo_data, f)


# Load GeoJSON file
with open("map.geojson", "r") as f:
    loaded_data = json.load(f)


print("\n=== VALID STATIONS ===")

max_temp = -999
max_name = ""
max_coords = []

for feature in loaded_data["features"]:
    properties = feature["properties"]
    name = properties["name"]
    temp = properties["temp"]

    if temp is not None:
        coords = feature["geometry"]["coordinates"]

        print(f"{name}: {temp}°C at ({coords[0]}, {coords[1]})")

        if temp > max_temp:
            max_temp = temp
            max_name = name
            max_coords = coords

print("\n=== HOTTEST STATION ===")
print(f"{max_name} has the highest temperature: {max_temp}°C")
print(f"Coordinates: ({max_coords[0]}, {max_coords[1]})")
