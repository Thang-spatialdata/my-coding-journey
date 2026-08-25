import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("stations.geojson")
gdf.plot(column="temp", cmap="coolwarm", legend=True)
plt.title("Station Map With Legend")
plt.show()
