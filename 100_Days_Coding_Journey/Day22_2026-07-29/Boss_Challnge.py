stations = [
    ("HY01", 28, (20.65, 106.05)),
    ("HY02", 31, (20.70, 106.10)),
    ("HY03", 29, (20.72, 106.15)),
    ("HY04", 32, (20.75, 106.20))
]

print("=== STATION LIST ===")

for name, temp, coords in stations:
    lat, lon = coords
    print(f"Station: {name} | Temperature: {temp}°C | Coordinates: ({lat}, {lon})")

# Count hot stations and create hot station list
count = 0
hot_stations = []
temperatures = []

for name, temp, coords in stations:
    temperatures.append(temp)

    if temp >= 30:
        count += 1
        hot_stations.append(name)

# Calculate average temperature
avg_temp = sum(temperatures) / len(temperatures)

print("\n=== OBSERVATION REPORT ===")
print(f"Number of hot stations: {count}")
print(f"Hot station list: {', '.join(hot_stations)}")
print(f"Average temperature: {avg_temp:.2f}°C")
