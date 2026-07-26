stations = ["HY01", "HY02", "HY03"]

temperatures = [28, 31, 29]

for station, temperature in zip(stations, temperatures):
    if temperature >= 30:
        print(f"{station}: {temperature}°C (Hot)")
    else:
        print(f"{station}: {temperature}°C")
