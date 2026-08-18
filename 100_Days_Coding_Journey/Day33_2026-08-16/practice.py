import geopandas as gpd
from shapely.geometry import Point

# Exercise 1
point = Point(106.0, 20.5)

print("Exercise 1")
print(point)


# Exercise 2
station_data = {
    "name": ["Station A", "Station B"],
    "geometry": [
        Point(106.0, 20.5),
        Point(105.85, 21.03)
    ]
}

gdf = gpd.GeoDataFrame(
    station_data,
    crs="EPSG:4326"
)

print("\nExercise 2")
print(gdf)


# Exercise 3
gdf_meters = gdf.to_crs(epsg=3857)

print("\nExercise 3")
print(gdf_meters.geometry)
