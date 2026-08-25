import json
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show

# Create boundary.geojson first — this file was not created in any previous lesson
boundary_geo = {
    "type": "Feature",
    "properties": {"name": "boundary"},
    "geometry": {
        "type": "Polygon",
        "coordinates": [[[105.7, 20.85], [106.15, 20.85], [106.15, 21.1], [105.7, 21.1], [105.7, 20.85]]]
    }
}
with open("boundary.geojson", "w") as file:
    json.dump(boundary_geo, file)

gdf_stations = gpd.read_file("stations.geojson")
boundary_gdf = gpd.read_file("boundary.geojson")

fig, ax = plt.subplots(figsize=(10, 8))

with rasterio.open("dem.tif") as dataset:
    show(dataset, ax=ax, cmap="gray")

boundary_gdf.plot(ax=ax, color="none", edgecolor="black", linewidth=0.5)
gdf_stations.plot(ax=ax, column="temp", cmap="coolwarm", markersize=36, legend=True)

plt.title("Vector + Raster Overlay With Boundary")
plt.savefig("overlay_map.png", dpi=300)
plt.show()
