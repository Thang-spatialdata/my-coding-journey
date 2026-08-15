import geopandas as gpd
import json

geo_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "HY01",
                "temp": 28
            },
            "geometry": {
                "type": "Point",
                "coordinates": [105.85, 21.03]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "HY02",
                "temp": 33
            },
            "geometry": {
                "type": "Point",
                "coordinates": [106.68, 20.85]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "HY03",
                "temp": 19
            },
            "geometry": {
                "type": "Point",
                "coordinates": [106.20, 20.60]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "HY04",
                "temp": 31
            },
            "geometry": {
                "type": "Point",
                "coordinates": [106.05, 20.95]
            }
        }
    ]
}

with open("stations_full.geojson", "w") as file:
    json.dump(geo_data, file)

try:
    gdf = gpd.read_file("stations_full.geojson")

    hot_stations = gdf[gdf["temp"] >= 30]

    temp_mean = gdf["temp"].mean()
    temp_max = gdf["temp"].max()

    hot_stations.to_file(
        "hot_stations.geojson",
        driver="GeoJSON"
    )

    print("\n===== Station Statistics Report =====")
    print(f"Total stations: {len(gdf)}")
    print(f"Hot stations: {len(hot_stations)}")
    print(f"Average temperature: {temp_mean:.2f}°C")
    print(f"Maximum temperature: {temp_max:.2f}°C")

except FileNotFoundError:
    print("Error: 'stations_full.geojson' not found")

except Exception as e:
    print(f"System error: {e}")
