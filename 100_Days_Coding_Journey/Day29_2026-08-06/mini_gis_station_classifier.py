# Mini GIS — Station Classifier

station_temps = {
    "HY01": 28,
    "HY02": 33,
    "HY03": 19,
    "HY04": 31,
    "HY05": 22
}

hot_stations = {
    name: temp
    for name, temp in station_temps.items()
    if temp >= 30
}

cold_stations = {
    name: temp
    for name, temp in station_temps.items()
    if temp < 25
}

print(f"Hot stations: {hot_stations}")
print(f"Total number of hot stations: {len(hot_stations)}")

print(f"Cold stations: {cold_stations}")
print(f"Total number of cold stations: {len(cold_stations)}")
