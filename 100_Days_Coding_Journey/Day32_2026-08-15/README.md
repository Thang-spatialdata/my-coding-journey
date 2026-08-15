# Day 32 - GeoPandas Basics

## 📚 What I Learned

Today I started working with **GeoPandas**, a Python library for working with geospatial vector data.

### Topics

- GeoDataFrame
- Reading GeoJSON with `gpd.read_file()`
- Accessing columns
- Accessing geometry
- Filtering GeoDataFrames
- `.iterrows()`
- Basic statistics
- Exporting GeoJSON

---

## 💻 Mini GIS

### Station GeoDataFrame Explorer

I created a simple program to explore station data using GeoPandas.

### Tasks

- Read `stations.geojson`
- Count the total number of stations
- Display station names and coordinates
- Calculate the average temperature

---

## 🏆 Boss Challenge

### Station Data Statistics

I created a GeoJSON dataset containing several weather stations.

The program:

- Creates a GeoJSON file
- Reads the file using GeoPandas
- Filters stations with temperature ≥ 30°C
- Calculates the average temperature
- Finds the maximum temperature
- Exports hot stations to `hot_stations.geojson`
- Handles errors using `try/except`

---

## 🧠 Key Concepts

```python
gdf = gpd.read_file("stations_full.geojson")

hot_stations = gdf[gdf["temp"] >= 30]

temp_mean = gdf["temp"].mean()
temp_max = gdf["temp"].max()

hot_stations.to_file(
    "hot_stations.geojson",
    driver="GeoJSON"
)
