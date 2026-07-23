# Mini GIS #1

stations = [
    {"name": "HY01", "temperature": 30},
    {"name": "HY02", "temperature": 28},
    {"name": "HY03", "temperature": 31}
]

# Print all station names
print("Station names:")
for station in stations:
    print(station["name"])

print()

# Print the temperature of each station
print("Station temperatures:")
for station in stations:
    print(station["name"], "-", station["temperature"], "°C")

print()

# Add a new station
stations.append({"name": "HY04", "temperature": 29})

# Print the total number of stations
print("Total stations:", len(stations))
