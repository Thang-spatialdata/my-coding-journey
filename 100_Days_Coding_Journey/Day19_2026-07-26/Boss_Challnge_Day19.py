stations = [
    {"name": "HY01", "temperature": 28},
    {"name": "HY02", "temperature": 31},
    {"name": "HY03", "temperature": 29},
    {"name": "HY04", "temperature": 32},
    {"name": "HY05", "temperature": 27}
]

print("=== Weather Stations ===")

for index, station in enumerate(stations, start=1):
    print(f"{index}. {station['name']} - {station['temperature']}°C")

count = 0

for station in stations:
    if station["temperature"] >= 30:
        count += 1

print(f"\nStations with temperature >= 30°C: {count}")

temperatures = []

for station in stations:
    temperatures.append(station["temperature"])

average = sum(temperatures) / len(temperatures)

print(f"Average temperature: {average:.2f}°C")
print(f"Highest temperature: {max(temperatures)}°C")
print(f"Lowest temperature: {min(temperatures)}°C")
