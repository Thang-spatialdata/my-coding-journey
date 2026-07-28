# Day 21 - Boss Challenge
# GIS Temperature Monitoring System


stations = [
    "HY01",
    "HY02",
    "HY03",
    "HY04",
    "HY05"
]

temperatures = [
    28,
    31,
    29,
    35,
    30
]

# Combine station names and temperatures

station_data = list(zip(stations, temperatures))

# Create a Set for hot stations

hot_stations = set()


for station, temperature in station_data:

    if temperature >= 30:
        hot_stations.add(station)


# Calculate statistics

total_stations = len(stations)

hot_station_count = len(hot_stations)

highest_temperature = max(temperatures)

average_temperature = sum(temperatures) / len(temperatures)



# Report

print("=== Temperature Monitoring Report ===")

print("\nStation information:")

for station, temperature in station_data:
    print(station, "-", temperature, "C")


print("\nHot stations:")

for station in sorted(hot_stations):
    print(station)


print("\nTotal stations:", total_stations)

print("Hot stations:", hot_station_count)

print("Highest temperature:",
      highest_temperature,
      "C")

print("Average temperature:",
      round(average_temperature, 1),
      "C")
