import geopandas as gpd
from shapely.geometry import Point


# Station data
station_data = {
    "name": ["HY01", "HY02", "HY03", "HY04"],
    "lon": [105.85, 106.68, 106.20, 106.05],
    "lat": [21.03, 20.85, 20.60, 20.95],
    "temp": [28, 33, 19, 31]
}


# Define the center point
center_lon, center_lat = 106.0, 21.0


# Create spatial points
points = [
    Point(lon, lat)
    for lon, lat in zip(
        station_data["lon"],
        station_data["lat"]
    )
]


# Create GeoDataFrame
gdf = gpd.GeoDataFrame(
    station_data,
    geometry=points,
    crs="EPSG:4326"
)


# Create center point
center_point = Point(center_lon, center_lat)

center_gs = gpd.GeoSeries(
    [center_point],
    crs="EPSG:4326"
)


# Reproject to EPSG:3857
gdf_meters = gdf.to_crs("EPSG:3857")
center_meters = center_gs.to_crs("EPSG:3857")

center = center_meters.geometry[0]


# Calculate distance from each station to the center
distance_list_km = []

for point in gdf_meters.geometry:
    distance_km = point.distance(center) / 1000
    distance_list_km.append(distance_km)


# Print distance report
print("\n=== Station Distance Report ===")

for i in range(4):
    print(
        f"Station {gdf_meters['name'][i]}: "
        f"{distance_list_km[i]:.0f} km"
    )


# Find the nearest station
min_distance = min(distance_list_km)
nearest_index = distance_list_km.index(min_distance)
nearest_station = gdf_meters["name"][nearest_index]


print(
    f"Nearest station: "
    f"{nearest_station} ({min_distance:.0f} km)"
)
