# Day 31 - Introduction to Spatial Data

## 📚 What I Learned

Today I officially started **Phase 2 — Real GIS Concepts**.

### Main Topics

- Vector data (Point, Line, Polygon)
- Raster data (pixels and continuous surfaces)
- Coordinate Reference System (CRS)
- WGS84 (EPSG:4326)
- Common GIS file formats:
  - `.shp`
  - `.geojson`
  - `.tif`

---

## 🌍 Practice

### Concept Exercises

- Classify Vector vs Raster datasets
- Choose the correct library: GeoPandas/Shapely or Rasterio
- Explain why GIS datasets must share the same CRS before overlaying

---

## 💻 Mini GIS

### Vector Layer Simulation

Created a simple vector-like structure using only Python:

- Store coordinates with tuples
- Combine them into a dictionary
- Print station name, coordinates, and geometry type (`Point`)

---

## 🏆 Boss Challenge

### File Metadata Classifier

Automatically classified files into:

- **Vector** → `.shp`, `.geojson`
- **Raster** → `.tif`

Used **list comprehension + string methods** to generate a GIS-style classification report.

---

## 🚀 Progress

**Day 31 / 100 completed ✅**

🎉 Python foundations are now connected to **real GIS data concepts**.
