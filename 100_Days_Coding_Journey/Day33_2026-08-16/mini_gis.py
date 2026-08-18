import geopandas as gpd
from shapely.geometry import Point


# Create points for Hanoi and Hai Phong
hanoi_point = Point(105.8542, 21.0285)
haiphong_point = Point(106.6881, 20.8449)


# Create GeoDataFrame
gdf = gpd.GeoDataFrame(
    geometry=[hanoi_point, haiphong_point],
    crs="EPSG:4326"
)


# Reproject to a CRS using meters
gdf_meters = gdf.to_crs(epsg=3857)


# Get the two points
point_1 = gdf_meters.geometry[0]
point_2 = gdf_meters.geometry[1]


# Calculate distance in kilometers
distance_in_km = point_1.distance(point_2) / 1000


print(f"Distance: {distance_in_km:.0f} km")
