stations = ["HY01", "HY02", "HY03", "HY04", "HY05"]

temperatures = [28, 31, 29, 32, 27]

print("=== Weather Stations ===")

# Display all stations with numbers
for index, (station, temperature) in enumerate(zip(stations, temperatures), start=1):
    print(f"{index}. {station} - {temperature}°C")

# Count stations with temperature >= 30°C
hot_stations = 0

for temperature in temperatures:
    if temperature >= 30:
        hot_stations += 1

print(f"\nThere are {hot_stations} hot stations.")

# Temperature statistics
average_temperature = sum(temperatures) / len(temperatures)

print(f"Highest temperature: {max(temperatures)}°C")
print(f"Lowest temperature: {min(temperatures)}°C")
print(f"Average temperature: {average_temperature:.2f}°C")
