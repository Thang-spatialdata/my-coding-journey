import os

required_files = [
    "stations.csv",
    "boundary.geojson",
    "rainfall.csv"
]

found_count = 0
missing_count = 0
missing_files = []

for file in required_files:
    if os.path.exists(file):
        found_count += 1
    else:
        missing_count += 1
        missing_files.append(file)

print("\n=== File Check Report ===")
print(f"Found: {found_count}")
print(f"Missing: {missing_count}")
print(f"Missing files: {missing_files}")
