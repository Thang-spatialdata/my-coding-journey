import numpy as np
import rasterio
from rasterio.transform import from_bounds

elevation = np.array([
    [120, 125, 130, 128, 132],
    [118, 122, 127, 124, 129],
    [115, 119, 123, 121, 126],
    [110, 114, 118, 116, 120],
    [108, 112, 115, 113, 117]
], dtype="float32")


# Create DEM raster
with rasterio.open(
    "dem.tif",
    "w",
    driver="GTiff",
    height=5,
    width=5,
    count=1,
    dtype=elevation.dtype,
    crs="EPSG:4326",
    transform=from_bounds(
        105.8, 20.9,
        106.0, 21.1,
        5, 5
    )
) as dataset:
    dataset.write(elevation, 1)


# Read DEM raster
with rasterio.open("dem.tif") as dataset:
    band1 = dataset.read(1)
    saved_crs = dataset.crs
    saved_transform = dataset.transform
    saved_dtype = dataset.dtype


# Analyze elevation
max_elevation = np.max(band1)
min_elevation = np.min(band1)
mean_elevation = np.mean(band1)

high_zone = np.where(
    band1 > 120,
    band1,
    0
)

high_zone_count = np.sum(band1 > 120)


# Save high-elevation raster
with rasterio.open(
    "high_zone.tif",
    "w",
    driver="GTiff",
    height=high_zone.shape[0],
    width=high_zone.shape[1],
    count=1,
    dtype=saved_dtype,
    crs=saved_crs,
    transform=saved_transform
) as dataset:
    dataset.write(high_zone, 1)


# Final report
print("\n===== DEM Analysis Report =====")
print(f"Maximum elevation: {max_elevation} m")
print(f"Minimum elevation: {min_elevation} m")
print(f"Mean elevation: {mean_elevation:.2f} m")
print(f"High-elevation pixels: {high_zone_count}")
