# Day 21 - Mini GIS
# GIS Station Update Analysis


old_stations = {
    "HY01",
    "HY02",
    "HY03",
    "HY04"
}


new_stations = {
    "HY02",
    "HY03",
    "HY04",
    "HY05",
    "HY06"
}


# Find new stations
added_stations = new_stations - old_stations


# Find active stations
active_stations = old_stations & new_stations


print("=== GIS Station Update Report ===")


print("\nTotal old stations:", len(old_stations))

print("Total new stations:", len(new_stations))


print("\nNew stations added:")

for station in sorted(added_stations):
    print(station)


print("\nActive stations:")

for station in sorted(active_stations):
    print(station)


print("\nNew stations added:", len(added_stations))

print("Active stations:", len(active_stations))
