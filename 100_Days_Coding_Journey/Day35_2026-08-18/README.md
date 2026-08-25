Day 35 - GIS Map Visualization & Layer Overlay

📚 What I Learned
Today I focused on map visualization techniques in Python, bridging vector and raster data to build multi-layered map plots and interactive web maps.

Topics
- Quick plotting with `.plot()`
- Attribute-based styling using `column="temp"`, `cmap="coolwarm"`, and `legend=True`
- Multi-layer spatial mapping using Matplotlib `ax=ax` parameter
- Order of visual layers (z-index / drawing order)
- Raster visualization using `rasterio.plot.show()`
- Introduction to interactive web maps using `folium`

💻 Mini GIS
Station Map With Legend
I created a script to map weather station points colored by temperature with an embedded legend bar.

Tasks
- Read station spatial data from `stations.geojson`
- Plot point locations with color mapping based on temperature values
- Add a colorbar legend using `legend=True`
- Set map title using `plt.title()`

🏆 Boss Challenge
Vector + Raster Overlay With Boundary
I built a complete multi-layer map rendering script combining custom boundary geometry, elevation raster data, and station point features.

The program:
- Generates `boundary.geojson` dynamically for study area boundaries
- Loads vector station data and area boundary using GeoPandas
- Opens elevation raster (`dem.tif`) using Rasterio
- Overlays raster elevation as background layer using `rasterio.plot.show()`
- Draws transparent-fill boundary line over the raster
- Plots temperature-coded station points on top with legend
- Formats map layout and exports high-DPI output to `overlay_map.png`
- 
