import numpy as np
import rasterio
from rasterio.transform import from_bounds


# Exercise 1
elevation = np.array([
    [67, 26, 131],
    [105, 57, 112],
    [91, 97, 47]
])

print(elevation)
print(elevation.shape)
print(elevation.mean())


# Exercise 2
print(elevation[elevation > elevation.mean()])


# Exercise 3
with rasterio.open(
    "new_elevation.tif",
    "w",
    driver="GTiff",
    height=3,
    width=3,
    count=1,
    dtype=elevation.dtype,
    crs="EPSG:4326",
    transform=from_bounds(
        78.8, 10.6,
        108.1, 38.3,
        3, 3
    )
) as dataset:
    dataset.write(elevation, 1)


with rasterio.open("new_elevation.tif") as dataset:
    band1 = dataset.read(1)
    print(band1.shape)
