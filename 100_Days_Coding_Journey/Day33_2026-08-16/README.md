# Day 33 - Spatial Distance with GeoPandas & Shapely

## 📚 What I Learned

Today I learned how to work with spatial points and calculate distances using GeoPandas and Shapely.

### Topics

- Shapely `Point`
- Longitude and latitude
- Coordinate order `(x, y)`
- Coordinate Reference Systems (CRS)
- EPSG:4326
- EPSG:3857
- GeoDataFrame
- `.to_crs()`
- `.distance()`
- Spatial distance analysis
- Finding the nearest station

---

## 🧠 Key Concepts

### 1. Creating Points with Shapely

Shapely uses:

```python
Point(x, y)
