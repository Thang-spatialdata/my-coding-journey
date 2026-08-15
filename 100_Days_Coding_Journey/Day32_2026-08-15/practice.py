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
        }
    ]
}

with open("stations.geojson", "w") as file:
    json.dump(geo_data, file)


# Exercise 1
gdf = gpd.read_file("stations.geojson")

print("===== Exercise 1 =====")
print(gdf.head())


# Exercise 2
print("\n===== Exercise 2 =====")
print("Columns:")
print(gdf.columns)

print("\nCRS:")
print(gdf.crs)


# Exercise 3
hot_stations = gdf[gdf["temp"] >= 30]

print("\n===== Exercise 3 =====")
print("Stations with temperature >= 30°C:")
print(hot_stations)
