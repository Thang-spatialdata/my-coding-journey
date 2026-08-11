# Mini GIS — Vector Layer Simulation

station_1 = (10.5, 13.7)
station_2 = (11.1, 15.9)
station_3 = (17.2, 14.2)

vector_layer = {
    "Station A": (station_1, "Point"),
    "Station B": (station_2, "Point"),
    "Station C": (station_3, "Point")
}

for station_name, (coords, geometry_type) in vector_layer.items():
    print(f"{station_name}: Coordinates {coords}, Type: {geometry_type}")
