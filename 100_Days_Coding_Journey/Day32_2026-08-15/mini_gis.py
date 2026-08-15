import geopandas as gpd

gdf = gpd.read_file("stations.geojson")

print(f"Total stations: {len(gdf)}")

print("Station list:")

for index, row in gdf.iterrows():
    print(f"Station: {row['name']} | Coordinates: {row['geometry']}")

temp_mean = gdf["temp"].mean()

print(f"Average station temperature: {temp_mean:.2f}°C")
