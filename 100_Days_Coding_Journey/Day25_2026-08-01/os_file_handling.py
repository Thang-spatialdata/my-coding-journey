import os

# Practice 1 - Join Path
folder = "reports"
filename = "summary.txt"
full_path = os.path.join(folder, filename)
print(full_path)


# Practice 2 - Filter GIS Files
files = [
    "stations.csv",
    "readme.txt",
    "map.geojson",
    "notes.md"
]

for file in files:
    name, ext = os.path.splitext(file)

    if ext in (".csv", ".geojson"):
        print(file)


# Practice 3 - Check File
def check_file(filename):
    if os.path.exists(filename):
        print(f"Already exists: {filename}")
    else:
        print(f"Missing: {filename}")


check_file("stations.csv")
check_file("boundary.geojson")
