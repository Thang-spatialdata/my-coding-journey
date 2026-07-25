stations = [
    {"name": "HY01", "temperature": 28},
    {"name": "HY02", "temperature": 31},
    {"name": "HY03", "temperature": 29}
]

for index, station in enumerate(stations, start=1):
    print(f"{index}. {station['name']} - {station['temperature']}°C")
