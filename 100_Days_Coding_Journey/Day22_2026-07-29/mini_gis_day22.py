stations = [
    ("HY01", 20.65, 106.05),
    ("HY02", 20.70, 106.10),
    ("HY03", 20.72, 106.15)
]

print("=== Station Coordinates ===")

for code, lat, lon in stations:
    print(f"{code}: ({lat}, {lon})")
