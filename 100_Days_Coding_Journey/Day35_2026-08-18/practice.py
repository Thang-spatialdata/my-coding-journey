import geopandas as gpd
import matplotlib.pyplot as plt

# Exercise 1 — Basic plot with .plot()
print("===== Exercise 1 =====")
gdf_stations = gpd.read_file("stations.geojson")
gdf_stations.plot()
plt.show()

# Exercise 2 — Re-plot with column="temp", cmap="coolwarm", legend=True
print("\n===== Exercise 2 =====")
gdf_stations.plot(column="temp", cmap="coolwarm", legend=True)

# Exercise 3 — Add title using plt.title() and show map
print("\n===== Exercise 3 =====")
plt.title("Temperature Distribution Map")
plt.show()
