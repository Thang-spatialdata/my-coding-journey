# Day 17 - Mini GIS

stations = [
    {"name": "HY01", "temperature": 30},
    {"name": "HY02", "temperature": 27},
    {"name": "HY03", "temperature": 32},
    {"name": "HY04", "temperature": 29}
]

print("Weather Stations:")

for station in stations:
    print(f"Station {station['name']}: {station['temperature']}°C")

# Create a list of temperatures
temperatures = []

for station in stations:
    temperatures.append(station["temperature"])

print("\nHighest temperature:", max(temperatures), "°C")
print("Lowest temperature:", min(temperatures), "°C")
print("Total temperature:", sum(temperatures), "°C")
print("Average temperature:", sum(temperatures) / len(temperatures), "°C")
