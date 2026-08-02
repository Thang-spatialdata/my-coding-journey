import os

files = [
    "hy01_temp.csv",
    "hy02_temp.csv",
    "boundary.geojson",
    "readme.txt",
    "hy03_rain.csv",
    "map.geojson"
]

classified_files = {
    ".csv": [],
    ".geojson": [],
    ".txt": []
}

for file in files:
    name, ext = os.path.splitext(file)

    if ext in classified_files:
        classified_files[ext].append(file)

print("\n=== Data Field Report ===")
print(f".csv: {len(classified_files['.csv'])} files")
print(f".geojson: {len(classified_files['.geojson'])} files")
print(f".txt: {len(classified_files['.txt'])} files")
