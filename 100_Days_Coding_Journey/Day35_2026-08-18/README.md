Day 35 - GIS Map Visualization & Layer Overlay


📚 What I Learned

Today I focused on map visualization in Python: plotting static maps, styling vector features, and layering vector data over raster imagery.


Topics

- Quick plotting with `.plot()`

- Attribute coloring (`column`, `cmap="coolwarm"`, `legend=True`)

- Multi-layer mapping using Matplotlib `ax=ax`

- Drawing order (layering z-index)

- Raster plotting with `rasterio.plot.show()`

- Interactive web maps with `folium` (intro)


💻 Mini GIS

Station Map With Legend

Created a script to display weather stations colored by temperature with a colorbar legend.


Tasks

- Read `stations.geojson`

- Plot points colored by `temp` attribute

- Add legend bar & title (`plt.title()`)


🏆 Boss Challenge

Vector + Raster Overlay With Boundary

Built a multi-layer map combining a DEM raster background, boundary polygon, and weather station points.


Tasks

- Generate `boundary.geojson`

- Open elevation raster (`dem.tif`) with Rasterio as base layer

- Overlay boundary polygon (`edgecolor="black"`)

- Overlay station points colored by temperature

- Export map image to `overlay_map.png` (300 DPI)
- 
