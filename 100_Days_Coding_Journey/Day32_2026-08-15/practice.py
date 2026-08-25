import geopandas as gpd
import matplotlib.pyplot as plt

# Exercise 1 — Read "stations.geojson" and plot using simple .plot()
print("===== Exercise 1 =====")
gdf = gpd.read_file("stations.geojson")
gdf.plot()
plt.title("Exercise 1: Basic Plot")
plt.show()


# Exercise 2 — Re-plot with column="temp", cmap="coolwarm", legend=True
print("\n===== Exercise 2 =====")
gdf.plot(column="temp", cmap="coolwarm", legend=True)


# Exercise 3 — Add title using plt.title() for Exercise 2 map
print("\n===== Exercise 3 =====")
plt.title("Exercise 2 & 3: Station Temperature Map")
plt.show()
