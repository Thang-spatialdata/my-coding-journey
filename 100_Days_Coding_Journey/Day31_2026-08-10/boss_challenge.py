# Boss Challenge — File Metadata Classifier

file_list = [
    "boundary.shp",
    "elevation.tif",
    "rivers.geojson",
    "satellite.tif",
    "stations.geojson"
]

vector_files = [
    file for file in file_list
    if file.endswith(".shp") or file.endswith(".geojson")
]

raster_files = [
    file for file in file_list
    if file.endswith(".tif")
]

print("\n===== File Classification Report =====")

print(f"\n1. Vector files (Total: {len(vector_files)} files)")
for file in vector_files:
    print(f"   + {file}")

print(f"\n2. Raster files (Total: {len(raster_files)} files)")
for file in raster_files:
    print(f"   + {file}")
