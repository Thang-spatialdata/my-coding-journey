import numpy as np

elevation = np.array([
    [120, 125, 130, 128],
    [118, 122, 127, 124],
    [115, 119, 123, 121],
    [110, 114, 118, 116]
])

mean_elevation = np.mean(elevation)
max_elevation = np.max(elevation)
min_elevation = np.min(elevation)

pixels_above_120 = np.sum(elevation > 120)
percentage = (pixels_above_120 / elevation.size) * 100

print("===== Elevation Analysis =====")
print(f"Mean elevation: {mean_elevation:.2f} m")
print(f"Maximum elevation: {max_elevation} m")
print(f"Minimum elevation: {min_elevation} m")
print(f"Pixels above 120 m: {pixels_above_120}")
print(f"Percentage above 120 m: {percentage:.2f}%")
